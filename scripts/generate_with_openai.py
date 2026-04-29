#!/usr/bin/env python3
"""
示例脚本：generate_with_openai.py
说明：读取 prompts 目录中的 prompt 文本，替换占位符并调用 OpenAI 完成稿件生成。
请先设置环境变量 OPENAI_API_KEY。
"""
import os
import json
from pathlib import Path

try:
    from openai import OpenAI
except Exception:
    # 如果使用 openai 包不是必须的，请改为适配你自己的 SDK
    pass

PROMPTS_DIR = Path(__file__).resolve().parents[1] / 'prompts'
OUTPUT_DIR = Path(__file__).resolve().parents[1] / 'examples'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_prompt(name):
    p = PROMPTS_DIR / name
    return p.read_text(encoding='utf-8')


def simple_render(template, variables):
    # 简单的占位符替换，变量格式：{key}
    s = template
    for k, v in variables.items():
        s = s.replace('{' + k + '}', v)
    return s


def main():
    # 基本参数（请按需替换）
    model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print('ERROR: 请先设置 OPENAI_API_KEY 环境变量')
        return

    # 示例变量（实际使用请从表单或外部来源传入）
    vars = {
        '主题': '导板种植如何提升效率',
        '目标医生层级': '进阶医生',
        '写作目的': '卖课',
        '主推产品/课程': '导板实操班（8周）',
        '字数': '1200'
    }

    # 加载并渲染 prompt
    prompt_template = load_prompt('prompt_body_v2.txt')
    prompt = simple_render(prompt_template, vars)

    # 调用示例：使用 OpenAI 官方 SDK（此处为伪代码/示例）
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        resp = client.chat.completions.create(
            model=model,
            messages=[{'role':'system','content':load_prompt('system_prompt_v2.txt')},
                      {'role':'user','content':prompt}],
            max_tokens=2200
        )
        content = resp.choices[0].message.content
    except Exception as e:
        print('调用模型失败（请根据你使用的 SDK 调整脚本）。错误信息：', e)
        content = '【示例输出占位】\n请在本地使用正确的 SDK 和 API Key 调用模型以生成真实稿件。'

    out_file = OUTPUT_DIR / 'generated_article.md'
    out_file.write_text(content, encoding='utf-8')
    print('生成完成，输出：', out_file)

if __name__ == '__main__':
    main()
