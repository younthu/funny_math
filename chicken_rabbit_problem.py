from manim import *

class ChickenRabbitProblem(Scene):
    def construct(self):
        # 问题设置
        num_chickens = 5
        num_rabbits = 3
        total_heads = num_chickens + num_rabbits
        total_legs = num_chickens * 2 + num_rabbits * 4
        
        with self.voiceover(text="鸡兔同笼问题是一个经典的数学问题。题目是：") as tracker:
            # 标题
            title = Text("鸡兔同笼问题", font_size=48)
            self.play(Write(title))
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="笼子里有鸡和兔子共8只，它们共有26只脚。问鸡和兔子各有多少只？") as tracker:
            # 移动标题到上方
            self.play(title.animate.to_corner(UL))
            
            # 介绍问题
            problem_text = Text(
                f"笼子里有鸡和兔子共{total_heads}只，\n"
                f"它们共有{total_legs}只脚。\n"
                "问鸡和兔子各有多少只？",
                font_size=36,
                line_spacing=1.5
            ).next_to(title, DOWN, buff=0.5).align_to(title, LEFT)
            
            self.play(Write(problem_text))
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="我们可以用'兔子抬起前脚'的方法来解决这个问题。现在让我们来看看笼子里的鸡和兔子。") as tracker:
            # 显示鸡和兔子的文字
            animals_group = VGroup()
            for i in range(total_heads):
                if i < num_chickens:
                    # 鸡的文字表示
                    animal = Text("鸡", font_size=40, color=YELLOW).set_stroke(BLACK, 1)
                else:
                    # 兔子的文字表示
                    animal = Text("兔子", font_size=40, color=WHITE).set_stroke(BLACK, 1)
                animal.move_to(RIGHT * 3 * (i % 4) + DOWN * 2 * (i // 4))
                animals_group.add(animal)
            
            self.play(FadeOut(problem_text), Create(animals_group))
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="第一步：让所有兔子抬起前脚。") as tracker:
            # 第一步：兔子抬起脚
            step1_text = Text("第一步：让所有兔子抬起前脚", font_size=36).to_corner(UL).shift(DOWN * 1.5)
            self.play(Write(step1_text))
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="现在，所有兔子都抬起了前脚，地上只留下了鸡的两只脚和兔子的后脚。") as tracker:
            # 动画展示兔子抬起脚
            rabbit_legs_up = []
            for i in range(num_chickens, total_heads):
                rabbit = animals_group[i]
                # 兔子抬起前脚的动画效果
                legs_up = Text("兔子(抬起前脚)", font_size=40, color=WHITE).set_stroke(BLACK, 1)
                legs_up.move_to(rabbit.get_center())
                rabbit_legs_up.append(legs_up)
                
                self.play(Transform(rabbit, legs_up), run_time=0.5)
            
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="让我们来计算一下此时地上的脚数。") as tracker:
            # 计算此时地上的脚数
            legs_on_ground = total_legs - num_rabbits * 2
            step1_calc = Text(
                f"此时地上的脚数 = {total_legs} - {num_rabbits}×2 = {legs_on_ground}",
                font_size=30
            ).next_to(step1_text, DOWN, buff=0.5).align_to(step1_text, LEFT)
            
            self.play(Write(step1_calc))
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="第二步：计算兔子的数量。每只兔子抬起2只脚，总共抬起的脚数是总脚数减去总头数乘以2。") as tracker:
            # 第二步：计算兔子的数量
            step2_text = Text("第二步：计算兔子的数量", font_size=36).next_to(step1_calc, DOWN, buff=0.5).align_to(step1_text, LEFT)
            self.play(Write(step2_text))
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="用总共抬起的脚数除以2，就可以得到兔子的数量。") as tracker:
            # 解释如何计算兔子数量
            step2_calc = Text(
                f"兔子的数量 = (总脚数 - 总头数×2)÷2\n"
                f"兔子的数量 = ({total_legs} - {total_heads}×2)÷2 = {num_rabbits}",
                font_size=30
            ).next_to(step2_text, DOWN, buff=0.5).align_to(step1_text, LEFT)
            
            self.play(Write(step2_calc))
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="第三步：计算鸡的数量。用总头数减去兔子的数量，就得到了鸡的数量。") as tracker:
            # 第三步：计算鸡的数量
            step3_text = Text("第三步：计算鸡的数量", font_size=36).next_to(step2_calc, DOWN, buff=0.5).align_to(step1_text, LEFT)
            self.play(Write(step3_text))
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="让我们来完成这个计算。") as tracker:
            step3_calc = Text(
                f"鸡的数量 = 总头数 - 兔子的数量\n"
                f"鸡的数量 = {total_heads} - {num_rabbits} = {num_chickens}",
                font_size=30
            ).next_to(step3_text, DOWN, buff=0.5).align_to(step1_text, LEFT)
            
            self.play(Write(step3_calc))
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="最后，我们得到了答案：") as tracker:
            # 高亮显示结果
            result_text = Text(
                f"结果：鸡有{num_chickens}只，兔子有{num_rabbits}只",
                font_size=40,
                color=GREEN
            ).move_to(ORIGIN).shift(UP * 3)
            
            self.play(
                FadeOut(step1_text),
                FadeOut(step1_calc),
                FadeOut(step2_text),
                FadeOut(step2_calc),
                FadeOut(step3_text),
                FadeOut(step3_calc),
                Write(result_text)
            )
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="现在，让兔子放下前脚，我们来看看最终的结果。") as tracker:
            # 兔子放下脚，恢复原状
            for i in range(num_chickens, total_heads):
                rabbit = animals_group[i]
                original_rabbit = Text("兔子", font_size=40, color=WHITE).set_stroke(BLACK, 1)
                original_rabbit.move_to(rabbit.get_center())
                
                self.play(Transform(rabbit, original_rabbit), run_time=0.5)
            
            # 分组显示鸡和兔子
            chickens = VGroup(*[animals_group[i] for i in range(num_chickens)])
            rabbits = VGroup(*[animals_group[i] for i in range(num_chickens, total_heads)])
            
            self.play(
                chickens.animate.arrange(RIGHT, buff=1).move_to(LEFT * 3 + DOWN),
                rabbits.animate.arrange(RIGHT, buff=1).move_to(RIGHT * 3 + DOWN)
            )
            
            self.wait(tracker.remaining_duration())
        
        with self.voiceover(text="这里清楚地显示了鸡和兔子的数量。鸡兔同笼问题就这样解决了！") as tracker:
            # 显示鸡和兔子的数量标签
            chicken_label = Text(f"鸡: {num_chickens}只", font_size=30).next_to(chickens, DOWN, buff=0.5)
            rabbit_label = Text(f"兔子: {num_rabbits}只", font_size=30).next_to(rabbits, DOWN, buff=0.5)
            
            self.play(Write(chicken_label), Write(rabbit_label))
            self.wait(2)    