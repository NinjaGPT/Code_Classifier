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

[+] 大模型行业问答知识总结：数据向量化、RAG、langchain、Agent技术
https://aibard123.com/digest/2023/1207/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%A1%8C%E4%B8%9A%E9%97%AE%E7%AD%94%E7%9F%A5%E8%AF%86%E6%80%BB%E7%BB%93%E6%95%B0%E6%8D%AE%E5%90%91%E9%87%8F%E5%8C%96RAGlangchainAgent%E6%8A%80%E6%9C%AF/

[+] RAG应用12种调优策略
https://www.learnprompt.pro/article/rag-optimise
https://towardsdatascience.com/a-guide-on-12-tuning-strategies-for-production-ready-rag-applications-7ca646833439#a5e2

[+] Advanced RAG series: Indexing
https://mp.weixin.qq.com/s/io6OJ_vsSNDkIlLCGJl_5A

[+] RAG 应用案例
https://www.learnprompt.pro/article/rag-devvai

[+] RAG高阶技巧
https://zhuanlan.zhihu.com/p/680232507

[+] Local RAG API building
https://otmaneboughaba.com/posts/local-rag-api/
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
* RAG典型调用模式
```
模式一：非结构化数据通过Embedding Model把非结构化数据进行embedding存到向量数据库中，然后形成Construct Prompts给到LLM。LLM返回结果给到用户。

模式二：用户提出问题，下一步把问题通过Embedding Model向量化，然后保存到长时记忆数据库（向量数据库）中，然后调用LLM完成问题的回答，接下来将大模型的回答存到长时记忆数据库中，最后返回给用户。

模式三：用户问问题，下一步把问题通过Embedding Model向量化，然后从Cache中（向量数据库）查询类似的问题和答案，返回给用户。如果没有命中，则去和LLM交互。然后把LLM的回答存到Cache中，最后把回答返回给用户。
```
![Alt](https://mmbiz.qpic.cn/sz_mmbiz_png/ZQRiaaQzL4WFI4GjsCK7cDars16sgEctWdoicqN90axll0FPCIFAYlibAPgLPLx4IbM8ElnTbpKBGICicUDRVw7Pdw/640?wx_fmt=png)


