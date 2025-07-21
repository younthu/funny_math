# funny_math

## 年龄问题manim动画运行说明

### 依赖环境
- Python 3.13+
- manim（建议manimCE 0.17.x或1.x）
- 建议安装支持中文的字体（如“Microsoft YaHei”），否则动画中文字会乱码

### 运行方法
1. 安装依赖：
   ```bash
   pip install manim
   ```
2. 运行动画（低质量预览）：
   ```bash
   manim -pql age.py AgeScene
   ```
   - `-pql` 表示低质量预览，推荐调试时使用
   - `-pqh` 表示高质量输出，适合最终导出

3. 如果遇到中文乱码，请在age.py中将`CH_FONT`变量改为你本机已安装的中文字体名。

4. 生成的视频文件默认在`media/videos/`目录下。

### 常见问题
- **中文乱码**：请确保manim代码中`font`参数为本机已安装的中文字体。
- **找不到manim命令**：请检查manim是否已正确安装并加入PATH。
- **动画内容超出画面**：本动画已自动留出四周空白，若仍有问题可调整`MARGIN`参数。

Interesting mathematic quiz solutions in animation.
