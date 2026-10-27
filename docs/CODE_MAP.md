# 代码地图

> 最后更新：2026-10-27

## 总体结构

```text
git-wechat-animation/
├─ index.html              # 微信聊天界面、动画与脚本
├─ test-ui.py              # Playwright 浏览器验收
├─ README.md               # 玩法、Git 历史和运行说明
└─ docs/                   # 项目备忘与代码地图
```

## 逐文件核心内容

### `index.html`

- 用途：提供 375×720 的手机聊天界面和循环动画。
- 结构：状态栏、标题栏、聊天容器、时间药丸、消息气泡。
- 关键函数：`sleep`、`scrollToBottom`、`showTyping`、`appendMessage`、`playConversation`。
- 数据流：消息脚本 → 输入状态 → 气泡节点 → 自动滚动。
- 注意：`main` 使用微信绿色，`feat-neon` 使用青绿到紫色渐变。

### `test-ui.py`

- 用途：加载本地页面，验证初始气泡、输入状态、动画增长和页面错误。
- 输入：本地 8100 端口。
- 输出：全部断言通过时退出码为 0。
