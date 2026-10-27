# 微信聊天动画：Git 代码时光机

这是一个 375×720 的微信风格聊天动画，用于练习 Git 版本管理。页面使用纯 HTML、CSS 和 JavaScript，无第三方依赖，直接用浏览器打开 `index.html` 即可运行。

## 功能

- 微信风格标题栏、状态栏、左右消息气泡和头像
- 七句对话自动循环播放
- 对方发送前显示绿色“对方正在输入”和省略号动效
- 消息逐条弹出，聊天区自动滚动到底部
- 药丸式时间分割线、气泡尾巴和柔和阴影
- 支持 `prefers-reduced-motion`

## Git 时间线

```text
docs: define Git chat animation design
v1 静态聊天界面
v2 消息自动播放动画
v3 优化细节与主题
feat-neon 霓虹渐变气泡与赛博朋克标题栏
```

本地版本实验还包括一次未提交的红色气泡改坏，随后用下面的命令恢复：

```bash
git checkout -- index.html
# 或
git reset --hard HEAD
```

查看完整提交和分支：

```bash
git log --oneline --graph --all
```

## 运行与验证

```bash
python -m http.server 8100 --bind 127.0.0.1
python test-ui.py
```

验证命令需要 Playwright 和 Microsoft Edge。访问地址为 `http://127.0.0.1:8100`。

## 分支说明

- `main`：v3 绿色气泡版本。
- `feat-neon`：在 v3 基础上开发的霓虹渐变版本，等待合并请求评审。
