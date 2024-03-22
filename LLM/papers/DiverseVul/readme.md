# DiverseVul
### A New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection
https://arxiv.org/pdf/2304.00409.pdf
---
```
1. LLM优于GNN（如ReVeal Model），数据集越大LLM优势越大，小数据集没有优势
2. T5 family（T5 base, code5 small，code5 base，NatGen）是最好的
3. 收集更多训练数据对性能提升不大，增益饱和，对泛化有帮助。
4. 增加来自相同分布的训练数据集体积有助于漏洞检测（提前知道测试数据的分布模型）
4. 特定于代码的预训练任务，是改进基于深度学习的漏洞检测的研究方向，这比模型大小更重要
5. 泛化挑战：检测在训练集中未出现过的项目，性能大幅下降，可能是拟合了训练集出现项目的模式或编码习惯
6. 训练数据标签噪声：主要问题是分布在多个函数中的漏洞，以及修复提交中对非安全漏洞问题的更改
7. 手工标注标签：时间成本很高，主要审查标记哪些commit是修复安全漏洞的，哪些不是；
8. encoder-decoder架构优于encoder / decoder架构
9. 权重（weighting），class weights最好的方案，在可见/未可见项目均得到性能提升，CodeT5 small得分最高
10.CWE，不同CWE学习难度不同，与训练数据大小无关
11.缺陷：标签噪声、空白commit视为安全修复、测试集污染风险
```
* Model参数比较
  
<img width="683" alt="image" src="https://github.com/NinjaGPT/Code_Classifier/assets/4035112/377f3cd1-1a8b-48d0-b78a-bc9b5212bd77">


* 不同CWE学习难度不同，与训练数据大小无关
  
![image](https://github.com/NinjaGPT/Code_Classifier/assets/4035112/33c51ccf-d07e-47d2-864c-aebd908f9397)

