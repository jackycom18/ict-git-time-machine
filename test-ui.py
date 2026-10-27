from playwright.sync_api import sync_playwright


def main() -> None:
    """功能：验证聊天界面、自动消息播放和输入状态。输入：无。输出：无，断言失败时抛出异常。"""
    errors: list[str] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page(viewport={"width": 900, "height": 900})
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto("http://127.0.0.1:8100", wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(500)
        assert page.title() == "码道小助手"
        assert page.locator(".bubble").count() == 2
        assert page.locator(".bubble.me").count() == 1
        assert "rgb(149, 236, 105)" in page.locator(".bubble.me").first.evaluate(
            "element => getComputedStyle(element).backgroundColor"
        ).lower()
        page.wait_for_selector(".typing", timeout=5000)
        typing_label = page.locator(".typing-label")
        assert typing_label.inner_text() == "对方正在输入"
        assert "rgb(37, 132, 68)" in typing_label.evaluate(
            "element => getComputedStyle(element).color"
        )
        assert page.locator(".bubble").first.evaluate(
            "element => getComputedStyle(element, '::before').content"
        ) == '""'
        assert page.locator(".time-pill").evaluate(
            "element => getComputedStyle(element).borderRadius"
        ) != "0px"
        page.wait_for_function(
            "document.querySelectorAll('.bubble').length >= 4",
            timeout=12000,
        )
        assert page.locator(".bubble").count() >= 4
        assert not errors, "page errors: " + "; ".join(errors)
        browser.close()


if __name__ == "__main__":
    main()
