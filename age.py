from manim import *

# 请确保你的系统已安装"Microsoft YaHei"或替换为本机可用的中文字体
CH_FONT = "Microsoft YaHei"

# 50px约等于manim默认分辨率下的0.9单位
MARGIN = 0.9

class AgeScene(Scene):
    def construct(self):
        # 内容整体组，便于缩放和居中
        content = VGroup()

        # 1. 题目字幕，剧中显示
        title = Text(
            "题目: 哥哥16岁时弟弟10岁，请问两人年龄之和为50时哥哥和弟弟各多少岁？",
            font=CH_FONT, font_size=36
        )
        title.move_to(UP * 2.5)
        content.add(title)
        self.play(Write(title))
        self.wait(1.2)

        # 2. 计算年龄差动画
        diff_text = Text("哥哥比弟弟大6岁：16 - 10 = 6", font=CH_FONT, font_size=32)
        diff_text.next_to(title, DOWN, buff=0.8)
        content.add(diff_text)
        self.play(Write(diff_text))
        self.wait(1.0)

        # 3. 弟弟的年龄用方框表示
        bro_label = Text("弟弟：", font=CH_FONT, font_size=32)
        bro_box = Square(side_length=1.2, color=BLUE)
        bro_group = VGroup(bro_label, bro_box).arrange(RIGHT, buff=0.3)
        bro_group.move_to(UP * 0.7)
        content.add(bro_group)
        self.play(FadeIn(bro_label), FadeIn(bro_box))
        self.wait(0.7)

        # 4. 哥哥的年龄用方框+6表示
        bro2_label = Text("哥哥：", font=CH_FONT, font_size=32)
        bro2_box = Square(side_length=1.2, color=GREEN)
        plus6 = Text("+ 6", font=CH_FONT, font_size=32, color=YELLOW)
        bro2_group = VGroup(bro2_label, bro2_box, plus6).arrange(RIGHT, buff=0.3)
        bro2_group.next_to(bro_group, DOWN, buff=0.8).align_to(bro_group, LEFT)
        content.add(bro2_group)
        self.play(FadeIn(bro2_label), FadeIn(bro2_box), FadeIn(plus6))
        self.wait(0.7)

        # 5. 大方框包围两人年龄，标记总和50
        both_groups = VGroup(bro_group, bro2_group)
        big_rect = SurroundingRectangle(both_groups, color=ORANGE, buff=0.4)
        sum_label = Text("总和50", font=CH_FONT, font_size=28, color=ORANGE)
        sum_label.next_to(big_rect, RIGHT, buff=0.3)
        content.add(big_rect, sum_label)
        self.play(Create(big_rect), FadeIn(sum_label))
        self.wait(0.7)

        # 6. 把+6移出来, 变成-6, 放50后面，表示成50-6，哥哥那一行的方框保留
        minus6 = Text("- 6", font=CH_FONT, font_size=32, color=YELLOW)
        minus6.next_to(sum_label, RIGHT, buff=0.2)
        self.play(
            plus6.animate.move_to(minus6.get_center()),
            run_time=1.0
        )
        self.wait(0.2)
        self.play(FadeIn(minus6))
        self.wait(0.4)

        # 7. 50 - 6 = 44
        eq1 = Text("50 - 6 = 44", font=CH_FONT, font_size=38)
        eq1.next_to(minus6, RIGHT, buff=0.4)
        content.add(eq1)
        self.play(Write(eq1))
        self.wait(0.7)

        # 8. 大方框里的两个小方框的和就是44
        # 重新出现两个小方框
        box1 = Square(side_length=1.2, color=BLUE)
        box2 = Square(side_length=1.2, color=GREEN)
        both_boxes = VGroup(box1, box2).arrange(DOWN, buff=1.1)
        both_boxes.move_to(DOWN * 0.7)
        content.add(box1, box2)
        self.play(FadeIn(box1), FadeIn(box2))
        brace = Brace(both_boxes, direction=RIGHT, color=ORANGE)
        brace_text = Text("共44", font=CH_FONT, font_size=28, color=ORANGE).next_to(brace, RIGHT)
        content.add(brace, brace_text)
        self.play(Create(brace), FadeIn(brace_text))
        self.wait(0.7)

        # 9. 一个小方框就是22
        eq2 = Text("44 ÷ 2 = 22", font=CH_FONT, font_size=38).next_to(brace_text, RIGHT, buff=0.6)
        content.add(eq2)
        self.play(Write(eq2))
        self.wait(0.7)

        # 10. 弟弟的年龄就是22
        bro22 = Text("弟弟 = 22", font=CH_FONT, font_size=32, color=BLUE)
        bro22.next_to(box1, LEFT, buff=1.2)
        content.add(bro22)
        self.play(FadeIn(bro22))
        self.wait(0.4)

        # 11. 哥哥的年龄就是22+6=28
        bro28 = Text("哥哥 = 22 + 6 = 28", font=CH_FONT, font_size=32, color=GREEN)
        bro28.next_to(box2, LEFT, buff=1.2)
        content.add(bro28)
        self.play(FadeIn(bro28))
        self.wait(0.8)

        # 内容整体缩放/居中，留出四周空白
        content.scale_to_fit_height(config.frame_height - 2 * MARGIN)
        content.scale_to_fit_width(config.frame_width - 2 * MARGIN)
        content.move_to(ORIGIN)

        # 12. 绿色✅和100分动画
        check = Text("✅", font=CH_FONT, font_size=120, color=GREEN).move_to(ORIGIN)
        score = Text("100分", font=CH_FONT, font_size=80, color=YELLOW).next_to(check, DOWN, buff=0.3)
        self.play(FadeOut(content))
        self.wait(0.2)
        self.play(GrowFromCenter(check), FadeIn(score, shift=UP), run_time=1.2)
        self.wait(1.2)

# 运行命令（终端执行）:
# manim -pql age.py AgeScene
# 如需高质量输出可用 -pqh
