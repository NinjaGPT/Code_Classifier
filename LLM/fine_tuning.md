# Fine Tuning
---
* ARTICLE
```
[+] What's Fine Tune?
https://www.appen.com.cn/blog/fine-tuning/

[+] Fine Tune Introduction
https://www.wehelpwin.com/article/4231

[+] Understanding Fine Tuning
https://blog.csdn.net/qq_45652492/article/details/123379156

[+] Fine Tuning All in One
https://blog.csdn.net/Julialove102123/article/details/135700402

[+] Three methods of fine tuning
https://zhuanlan.zhihu.com/p/620618701

[+] Methods and frameworks
https://note.iawen.com/note/llm/finetune

[+] How to FT?
https://pytorch-tutorial.readthedocs.io/en/latest/tutorial/chapter04_advanced/4_1_fine-tuning/

[+] FT with GPT
https://platform.openai.com/docs/guides/fine-tuning
https://openai.xiniushu.com/docs/guides/fine-tuning
https://platform.openai.com/docs/api-reference/fine-tuning
https://mp.weixin.qq.com/s/jwL_j-qSjEcpT0yWtBtHYA
https://blog.csdn.net/gerouhsius/article/details/135582250

[+] Custom Model via LangChain & Fine Tune  
https://blog.csdn.net/m0_66076989/article/details/135346212

[+] PyTorch Tutorial
https://github.com/yunjey/pytorch-tutorial
https://github.com/zergtant/pytorch-handbook
```
* VIDEO
```
[+] 10分钟教你如何做chatGPT微调Fine-Tune
https://www.youtube.com/watch?v=TTrYhNRUpwo

[+] 提示词、RAG、微调
https://www.youtube.com/watch?v=P1iob2uKFrg&t=1220s

[+] 大语言模型微调之道 - 系列教程 （deeplearning.ai）
https://www.youtube.com/playlist?list=PLiuLMb-dLdWKtPM1YahmDHOjKN_a2Uiev

[+] OpenAI fine-tuning no need coding
https://www.youtube.com/watch?v=yyfsCLku1_s

[+] Fine Tuning GPT
https://www.youtube.com/watch?v=5vvtohsuo6A

[+] LLAMA2 Fine Tuning
https://www.youtube.com/watch?v=LslC2nKEEGU
```
---
## [ ⚠️ ] Supervised & Unsupervised (训练数据来源与特点分类)：
### 监督式微调 SFT(Supervised Fine Tuning)
  用人工标注的数据，用传统机器学习中监督学习的方法，对大模型进行微调；
  
### 基于人类反馈的强化学习微调 RLHF(Reinforcement Learning with Human Feedback)
  把人类的反馈，通过强化学习的方式，引入到对大模型的微调中去，让大模型生成的结果，更加符合人类的一些期望
  
### 基于AI反馈的强化学习微调 RLAIF(Reinforcement Learning with AI Feedback)
  跟RLHF类似，但是反馈的来源是AI。这里是想解决反馈系统的效率问题，因为收集人类反馈，相对来说成本会比较高、效率比较低

---
## [ ⚠️ ] 微调预训练模型的方法：
• 微调所有层：将预训练模型的所有层都参与微调，以适应新的任务。

• 微调顶层：只微调预训练模型的顶层，以适应新的任务。

• 冻结底层：将预训练模型的底层固定不变，只对顶层进行微调。

• 逐层微调：从底层开始，逐层微调预训练模型，直到所有层都被微调。

• 迁移学习：将预训练模型的知识迁移到新的任务中，以提高模型性能。这种方法通常使用微调顶层或冻结底层的方法。

---
## [ ⚠️ ] Full Fine Tuning (全参数微调)
以BERT模型为代表的“预训练语言模型 + 下游任务微调”训练模式成为了自然语言处理研究和应用的新范式。此处的下游任务微调是基于模型全量参数进行微调。
以 ChatGPT 为代表的预训练语言模型（PLM）规模变得越来越大，在消费级硬件上进行全量微调（Full Fine-Tuning）变得不可行。
此外，为每个下游任务单独存储和部署微调模型变得非常昂贵，因为微调模型与原始预训练模型的大小相同。
此外，模型全量微调还会损失多样性，存在灾难性遗忘的问题。
因此，如何高效的进行模型微调就成了业界研究的重点，这也为参数高效微调技术的快速发展带来了研究空间

---

## [ ⚠️ ] Parameter-Efficient Fine-Tuning (PEFT, 参数高效微调) / "Repurposing" 部分微调
    REFERENCE: Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning: https://arxiv.org/pdf/2303.15647.pdf
    
  ![Alt xxx](https://img-blog.csdnimg.cn/direct/d46aa699d7954cb592059b737490d54a.png)
    
### PEFT 方法可以分为三类，不同的方法对模型的不同部分进行下游任务的适配：

#### Prefix/Prompt-Tuning：
在模型的输入或隐层添加 k 个额外可训练的前缀 tokens（这些前缀是连续的伪 tokens，不对应真实的 tokens），只训练这些前缀参数；

#### Adapter-Tuning：
将较小的神经网络层或模块插入预训练模型的每一层，这些新插入的神经模块称为 adapter（适配器），下游任务微调时也只训练这些适配器参数；

#### LoRA：
通过学习小参数的低秩矩阵来近似模型权重矩阵 W 的参数更新，训练时只优化低秩矩阵参数。

```
常见的参数高效微调技术有BitFit、Prefix Tuning、Prompt Tuning、P-Tuning、Adapter Tuning、LoRA等

增加额外参数，如：Prefix Tuning、Prompt Tuning、Adapter Tuning及其变体。
选取一部分参数更新，如：BitFit。
引入重参数化，如：LoRA、AdaLoRA、QLoRA。
混合高效微调，如：MAM Adapter、UniPELT。
```

---
## [ ⚠️ ] 常见PEFT技术介绍
### BitFit
  对微调机制的一种积极探索，也很简单，通过仅调整bias效果就能有不错的效果，但没有具体阐述原理，就是通过猜测加实验得到的结果。
  同时，作者提出一个观点：微调的过程不是让模型适应另外的数据分布，而是让模型更好的应用出本身的表征能力。
```
特点：训练参数量极小（约0.1%）。 在大部分任务上效果会差于LoRA、Adapter等方法。
```

### Prefix tuning
  出发点跟Prompt Tuning类似, 具体实现有些差异;Prompt Tuning是在Embedding环节，往输入序列X前面加特定的Token;而Prefix Tuning是在Transformer的Encoder和Decoder的网络中都加了一些特定的前缀。
  REFERENCE: Prefix-Tuning: Optimizing Continuous Prompts for Generation: https://arxiv.org/pdf/2101.00190.pdf
```
特点： 前缀Token会占用序列长度，有一定的额外计算开销。 Prefix Tuning的线性插值是比较复杂的。
```

### Prompt-Tuning
  基座模型(Foundation Model)的参数不变，为每个特定任务，训练一个少量参数的小模型，在具体执行特定任务的时候按需调用。
  REFERENCE: The Power of Scale for Parameter-Efficient Prompt Tuning: https://arxiv.org/pdf/2104.08691.pdf
```
特点：相对于Prefix Tuning，参与训练的参数量和改变的参数量更小，更节省显存。 对一些简单的NLU
任务还不错，但对硬序列标记任务（即序列标注）表现欠佳。
```

### P-Tuning
将Prompt转换为可以学习的Embedding层，并用MLP+LSTM的方式来对Prompt Embedding进行一层处理。
相比Prefix Tuning，仅在输入层加入的可微的virtual token；另外，virtual token的位置也不一定是前缀，插入的位置是可选的。
```
特点：引入一个prompt encoder（由一个双向的LSTM+两层MLP组成）来建模virtual token的相互依赖会收敛更快，效果更好。
```

### P-Tuning v2
该方法在每一个Transformer层都加入了prompt token作为输入，引入多任务学习，针对不同任务采用不同的提示长度。并且回归传统的分类标签范式，而不是映射器。
```
特点：解决了Prompt Tuning无法在小模型上有效提升的问题。 移除了对模型效果改进较小的重参数化的编码器（如：Prefix Tuning中的MLP、P-Tuning中的LSTM）。 对于一些复杂的硬序列标记任务（即序列标注）取得了不错的效果。
```

### Adapter Tuning
该方法设计了Adapter结构，并将其嵌入Transformer的结构里面，针对每一个Transformer层，增加了两个Adapter结构，在训练时，固定住原来预训练模型的参数不变，只对新增的Adapter结构和Layer Norm 层进行微调。
```
特点：通过在Transformer层中嵌入Adapter结构，在推理时会额外增加推理时长。
```

### AdapterFusion
一种融合多任务信息的Adapter的变体，在 Adapter 的基础上进行优化，通过将学习过程分为两阶段来提升下游任务表现。

### AdapterDrop
该方法在不影响任务性能的情况下，对Adapter动态高效的移除，尽可能的减少模型的参数量，提高模型在反向传播（训练）和正向传播（推理）时的效率。
```
特点： 通过从较低的 Transformer 层删除可变数量的Adaper来提升推理速度。
当对多个任务执行推理时，动态地减少了运行时的计算开销，并在很大程度上保持了任务性能。
```

### LoRA
  大模型参数很多，但并不是所有的参数都是发挥同样作用的；大模型中有其中一部分参数，是非常重要的，是影响大模型生成结果的关键参数，这部分关键参数就是上面提到的低维的本质模型
  
  REFERENCE: LoRA: Low-Rank Adaptation of Large Language Models: https://arxiv.org/pdf/2106.09685.pdf
```
特点：将BA加到W上可以消除推理延迟。 可以通过可插拔的形式切换到不同的任务。 设计的比较好，简单且效果好。
```

### AdaLoRA
对LoRA的一种改进，它根据重要性评分动态分配参数预算给权重矩阵，将关键的增量矩阵分配高秩以捕捉更精细和任务特定的信息，而将较不重要的矩阵的秩降低，以防止过拟合并节省计算预算。

### QLoRA (Quantization)
  Quantization量化，是一种在保证模型效果基本不降低的前提下，通过降低参数的精度，来减少模型对于计算资源的需求的方法。量化的核心目标是降成本，降训练成本，特别是降后期的推理成本。
  
  REFERENCE: QLoRA: Efficient Finetuning of Quantized LLMs: https://arxiv.org/pdf/2305.14314.pdf
```
特点：使用 QLoRA 微调模型，可以显著降低对于显存的要求。同时，模型训练的速度会慢于LoRA。
```

### MAM Adapter
一种在 Adapter、Prefix Tuning 和 LoRA 之间建立联系的统一方法。最终的模型 MAM Adapter 是用于 FFN 的并行 Adapter 和 软提示的组合。
```
特点：整体上来说，最终的模型MAM Adapter效果会优于单个高效微调方法。
```

### UniPELT
一种将不同的PELT方法LoRA、Prefix Tuning和Adapter作为子模块，并通过门控机制学习激活最适合当前数据或任务的方法。
```
特点：相对于LoRA，BitFit，Prefix-tuning，训练的参数量更大；同时，推理更耗时；并且，输入会占用额外的序列长度。 多种PELT 方法的混合涉及PLM 的不同部分对模型有效性和鲁棒性都有好处。
```
---
## [ ⚠️ ] Fine Tuning Process Summary:
大模型微调如上文所述有很多方法，并且对于每种方法都会有不同的微调流程、方式、准备工作和周期。然而大部分的大模型微调，都有以下几个主要步骤，并需要做相关的准备：

### 准备数据集：
收集和准备与目标任务相关的训练数据集。确保数据集质量和标注准确性，并进行必要的数据清洗和预处理。

### 选择预训练模型/基础模型：
根据目标任务的性质和数据集的特点，选择适合的预训练模型。

### 设定微调策略：
根据任务需求和可用资源，选择适当的微调策略。考虑是进行全微调还是部分微调，以及微调的层级和范围。

### 设置超参数：
确定微调过程中的超参数，如学习率、批量大小、训练轮数等。这些超参数的选择对微调的性能和收敛速度有重要影响。

### 初始化模型参数：
根据预训练模型的权重，初始化微调模型的参数。对于全微调，所有模型参数都会被随机初始化；对于部分微调，只有顶层或少数层的参数会被随机初始化。

### 进行微调训练：
使用准备好的数据集和微调策略，对模型进行训练。在训练过程中，根据设定的超参数和优化算法，逐渐调整模型参数以最小化损失函数。

### 模型评估和调优：
在训练过程中，使用验证集对模型进行定期评估，并根据评估结果调整超参数或微调策略。这有助于提高模型的性能和泛化能力。

### 测试模型性能：
在微调完成后，使用测试集对最终的微调模型进行评估，以获得最终的性能指标。这有助于评估模型在实际应用中的表现。

### 模型部署和应用：
将微调完成的模型部署到实际应用中，并进行进一步的优化和调整，以满足实际需求。
