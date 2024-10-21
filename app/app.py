import gradio as gr
import pandas as pd
import pickle

df_dict = {}
files = ['PS2', 'FS1']
for f in files:
    df_dict[f] = pd.read_csv(f'data/{f}.txt', sep='\t', header=None)
    
df_dict['PS2_mean'] = pd.DataFrame(df_dict['PS2'].mean(axis=1), columns=['mean_ps2'])
df_dict['FS1_mean'] = pd.DataFrame(df_dict['FS1'].mean(axis=1), columns=['mean_fs1'])

X_data = pd.concat([df_dict['PS2_mean'], df_dict['FS1_mean']], axis= 1)
scaler_model = pickle.load(open('scaler_file', 'rb'))
knn_model = pickle.load(open('knn_file', 'rb'))

def predict(idx):
    idx = int(idx)
    if idx < 0 or idx > len(X_data):
        return 'UNKNOWN CYCLE'
    norm_values = scaler_model.transform([X_data.iloc[idx].values])
    prediction = knn_model.predict(norm_values)[0].item()
    if prediction == 1:
        return 'Valve condition is non optimal'
    else:
        return 'Valve condition is optimal'

with gr.Blocks() as window:
    gr.Markdown("# THE CUTTING EDGE PREDICTOR")
    with gr.Row():
        input_idx = gr.Textbox(label="Enter the cycle number you want to predict :", interactive=True)
        output = gr.Text(label="Valve Status :")
    with gr.Row():
        pred_btn = gr.Button("Predict", interactive=True)
    with gr.Row():
        gr.ClearButton([input_idx, output])

    pred_btn.click(predict, inputs=input_idx, outputs=[output])

if __name__ == "__main__":
    window.launch()