import numpy as np
import joblib
from flask import Flask, render_template, request, jsonify
import os
# 获取当前脚本所在的文件夹路径
current_folder = os.path.dirname(os.path.abspath(__file__))

# 将工作路径设置为当前文件夹
os.chdir(current_folder)
app = Flask(__name__)

# 加载模型
model_dir = 'models'
failure_models = {}
for failure_class in [0, 1, 2]:
    model_path = os.path.join(model_dir, f'ngboost_model_failure_{failure_class}.joblib')
    failure_models[failure_class] = joblib.load(model_path)

# 加载分类器
classifier = joblib.load(os.path.join(model_dir, 'failure_classifier.joblib'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 获取用户输入
        data = request.json
        input_params = [
            float(data['H']),
            float(data['L_over_B']),
            float(data['fy']),
            float(data['fck']),
            float(data['Acfck']),
            float(data['Asfy'])
        ]
        
        # 转换为模型所需格式
        input_array = np.array([input_params])
        
        # 预测破坏模式
        failure_prediction = classifier.predict(input_array)[0]
        failure_probs = classifier.predict_proba(input_array)[0]
        
        # 获取承载力预测
        bearing_capacity_model = failure_models[failure_prediction]
        dist = bearing_capacity_model.pred_dist(input_array)
        mean_capacity = dist.mean()[0]
        std_capacity = dist.std()[0]
        
        # 准备结果
        result = {
            'failure_mode': int(failure_prediction),
            'failure_probabilities': {
                'Failure=0': float(failure_probs[0]),
                'Failure=1': float(failure_probs[1]),
                'Failure=2': float(failure_probs[2])
            },
            'bearing_capacity': float(mean_capacity),
            'capacity_uncertainty': {
                'mean': float(mean_capacity),
                'std_dev': float(std_capacity),
                '95%_CI': [float(mean_capacity - 1.96 * std_capacity), 
                           float(mean_capacity + 1.96 * std_capacity)]
            }
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)