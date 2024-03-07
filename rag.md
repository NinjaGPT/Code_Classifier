## RAG (Retrieval-Augmented Generation)

```
[+] 以3个难度级别解释向量数据库
https://towardsdatascience.com/explaining-vector-databases-in-3-levels-of-difficulty-fc392e48ab78
https://sihaiba.com/explaining-vector-databases-in-3-levels-of-difficulty.html

[+] Weaviate 入门：矢量数据库搜索初学者指南
https://towardsdatascience.com/getting-started-with-weaviate-a-beginners-guide-to-search-with-vector-databases-14bbb9285839

[+] 检索增强生成（RAG）：从理论到 LangChain 实践
https://towardsdatascience.com/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2

[+] Elasticsearch：特定领域的生成式 AI - 预训练、微调和 RAG
https://juejin.cn/post/7335093445868159013
https://www.elastic.co/search-labs/blog/articles/domain-specific-generative-ai-pre-training-fine-tuning-rag#domain-specific-pre-training
```
在 RAG 中，`事实性知识`与 LLM 的`推理能力`相分离，被存储在**容易访问** 和 **及时更新**的外部知识源中

* 参数化知识（Parametric knowledge）：  
模型在训练过程中学习得到的，隐式地储存在神经网络的权重中。

* 非参数化知识（Non-parametric knowledge）：  
存储在外部知识源，例如向量数据库中。

![Alt](https://baoyu.io/images/rag/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation/1_kSkeaXRvRzbJ9SrFZaMoOg.webp)
> 检索增强生成（RAG）的工作流程，从用户的查询开始，经过向量数据库的检索，到提示填充，最后生成回应。

* RAG 工作流程
```
1.检索： 此过程涉及利用用户的查询内容，从外部知识源获取相关信息。具体来说，就是将用户的查询通过嵌入模型转化为向量，以便与向量数据库中的其他上下文信息进行比对。通过这种相似性搜索，可以找到向量数据库中最匹配的前 k 个数据。
2.增强： 接着，将用户的查询和检索到的额外信息一起嵌入到一个预设的提示模板中。
3.生成： 最后，这个经过检索增强的提示内容会被输入到大语言模型 (LLM) 中，以生成所需的输出。

```




