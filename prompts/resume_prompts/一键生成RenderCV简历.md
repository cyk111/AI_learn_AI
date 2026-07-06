# 一键生成 RenderCV 简历

**用途**：从零到完整 YAML 简历，一键渲染 PDF
**适用模型**：Claude Sonnet 4.5 / Opus 4.8
**需要工具**：RenderCV (`pip install "rendercv[full]"`)

---

## Prompt

```text
你是世界顶级简历顾问。请基于以下信息，生成一份完整的 RenderCV 兼容 YAML 简历。

【个人信息】
姓名：
目标职位：
LinkedIn/网站：
邮箱：
电话：
城市：

【工作经历】（从最近到最早）
公司1：{名称} | {职位} | {起止日期}
- 我做了什么（具体行动）：
- 成果是什么（量化数字）：

公司2：...

【教育背景】
学校：{名称} | {学位} | {专业} | {毕业年份}

【技能】
技术栈：{按熟练度排列}
语言：{语言能力}
证书：{如有}

【项目/作品】（选 1-3 个最出彩的）
项目1：{名称} {链接}
- 描述：{1 句话}
- 成果：{量化数字}

【设计要求】
- 主题：moderncv（engineer）/ classic（academic）
- 强调色：#1A1A2E
- 语言：中文（locale: zh-CN）/ English（locale: en-US）
- 页数：严格 1 页

---

## 输出格式

请输出完整 RenderCV YAML，放在 ```yaml 代码块中。

Schema 参考：
```yaml
cv:
  name: "张三"
  label: "Senior Frontend Engineer"
  location: "Shanghai, China"
  email: "zhangsan@email.com"
  phone: "+86 138-0000-0000"
  website: "linkedin.com/in/zhangsan"
  
  sections:
    summary:
      - "3句话：身份 + 成就 + 方向"
    
    experience:
      - company: "公司名"
        position: "职位"
        location: "城市"
        start_date: "2022-01"
        end_date: "present"
        highlights:
          - "STAR bullet 1（含量化数字）"
          - "STAR bullet 2（含量化数字）"
          - "STAR bullet 3（含量化数字）"
    
    education:
      - institution: "大学名"
        degree: "BS"
        field: "Computer Science"
        start_date: "2018"
        end_date: "2022"
    
    skills:
      - label: "Languages"
        details: "TypeScript, Python, Go, Rust"
      - label: "Frameworks"
        details: "React, Next.js, Node.js"
    
    projects:
      - name: "项目名"
        url: "https://github.com/..."
        highlights:
          - "成果描述（含量化数字）"

design:
  theme: "moderncv"
  font: "Roboto"
  font_size: "10pt"
  page_size: "a4"
  color: "#1A1A2E"
```

【规则】
- 每条 work experience 写 3-5 个 highlights
- 每个 highlight 必须有量化数字（%、$、用户数、时间节省）
- 不确定的数字标注 [需要数据]，不要编造
- 英文：过去时态 + 强力动词（Led, Built, Shipped, Reduced, Scaled）
- 中文：结果导向 + 主动语态
- Summary 严格 3 句，总长 ≤ 300 字符
- 技能按熟练度从高到低排列
```

---

## 生成后操作

```bash
# 1. 将 AI 输出的 YAML 保存为 my_cv.yaml
# 2. 安装 RenderCV
pip install "rendercv[full]"

# 3. 渲染 PDF
rendercv render my_cv.yaml

# 4. 查看 PDF
open my_cv.pdf
```
