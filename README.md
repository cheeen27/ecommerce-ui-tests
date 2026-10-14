# E-commerce UI Automation Tests

基于 Python、pytest 和 Playwright 的电商网站 UI 自动化测试项目，使用 SauceDemo 作为测试对象，覆盖登录、商品展示及购物车等核心功能。

## 技术栈

- Python 3.12
- pytest
- Playwright
- pytest-html

## 测试范围

| 测试模块 | 测试场景 |
|---|---|
| 登录 | 正确账号登录成功 |
| 登录 | 错误密码时显示错误提示 |
| 商品 | 商品列表正常显示 |
| 购物车 | 添加商品后购物车数量更新 |
| 购物车 | 移除商品后购物车状态更新 |

## 环境准备

建议使用 Python 3.12。

```bash
git clone <your-repository-url>
cd ecommerce-ui-tests

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python -m playwright install chromium
```

## 运行测试

运行全部测试：

```bash
python -m pytest -v
```

生成 HTML 测试报告：

```bash
python -m pytest -v --html=report.html --self-contained-html
```

运行完成后，可以在项目根目录打开 `report.html` 查看测试结果。

## 项目结构

```text
ecommerce-ui-tests/
├── tests/
│   ├── conftest.py
│   └── test_login.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 项目说明

本项目用于练习 Web UI 自动化测试，包括测试用例设计、pytest fixture 复用、页面元素定位、断言及 HTML 测试报告生成。

测试对象为公开演示网站，测试结果可能受到网站页面调整或网络状态影响。