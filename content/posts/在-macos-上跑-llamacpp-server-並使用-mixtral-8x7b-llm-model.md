+++
title = "在 MacOS 上跑 llama.cpp server 並使用 Mixtral-8x7B LLM Model"
date = "2024-01-26T04:57:32.916Z"
description = "執行 server 時，要用下面的方式，同網路下的設備才存取得到"
slug = "在-macos-上跑-llamacpp-server-並使用-mixtral-8x7b-llm-model"
canonicalURL = "https://medium.com/@danielkao/%E5%9C%A8-macos-%E4%B8%8A%E8%B7%91-llama-cpp-server-%E4%B8%A6%E4%BD%BF%E7%94%A8-mixtral-8x7b-llm-model-9cc178cfbfa1"
mediumID = "9cc178cfbfa1"
+++

執行 server 時，要用下面的方式，同網路下的設備才存取得到

```
./server --host 0.0.0.0 --and_other_params
```
