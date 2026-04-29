# 口腔医生转化型公众号写作助手（EIYO1/gzh）

这是为口腔医生/种植方向打造的一套“成交型”写作 skill（prompts、示例脚本、话术库），包含系统提示、标准 prompt、案例模板、私信与短视频脚本、以及一个示例的 Python 调用脚本。

主要内容
- prompts/: 各类可直接调用的 prompt 文本
- examples/: 私信模板与短视频 hooks
- scripts/: 调用示例脚本（Python）

快速使用说明
1. 在本地安装 Python 与依赖：
   - Python 3.8+
   - pip install -r requirements.txt（若使用 OpenAI Python SDK）
2. 将 OpenAI Key 以环境变量形式设置：
   - export OPENAI_API_KEY="your_key_here"（Linux/Mac）
   - setx OPENAI_API_KEY "your_key_here"（Windows）
3. 修改 scripts/generate_with_openai.py 中的参数（model、prompt 路径、输出文件路径等），运行脚本生成文章草稿。

合规提醒
- 所有病例数据须去标识化或已取得书面授权；脚本与模板中包含合规提醒，请严格遵守当地医疗广告法规。
- 发布任何带数据/效果的内容时，务必注明“个案/学员反馈，不代表普遍结果”。

分支与提交
- 本次提交到分支: gzh

如需我将样稿一并生成并提交到 examples/，请在仓库分支上再发起一次请求并提供用户调用模板的数据。