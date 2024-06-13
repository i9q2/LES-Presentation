from manim import *
from manim_slides import Slide

class Presentation(Slide):
    def construct(self):


        heading_1 = Text('Lineares Gleichungssystem', font_size = 48, color = BLUE_B).move_to(UP)
        names = Text('Dmytro Chumak', font_size = 32).next_to(heading_1, DOWN*2)
        dateNplace = Text('IGS HES, 2024 Sommer', font_size = 32).next_to(names, DOWN)


        papyrus = ImageMobject(r'D:\DC\Desktop\LESManim\images\papyrus.png').move_to(DOWN / 4)
        papyrusName = Text('Papyrus Rhind', font_size = 32).move_to(UP * 3.5)
        papyrus.scale(0.9)


        diphantus = ImageMobject(r'D:\DC\Desktop\LESManim\images\diphantus.jpg').to_edge(LEFT, buff = 0.2)
        kharezmi = ImageMobject(r'D:\DC\Desktop\LESManim\images\kharezmi.jpg').next_to(diphantus, buff = 0.2)
        viete = ImageMobject(r'D:\DC\Desktop\LESManim\images\viete.jpg').next_to(kharezmi, buff = 0.2)
        hals = ImageMobject(r'D:\DC\Desktop\LESManim\images\hals.jpg').next_to(viete, buff = 0)
        gauss = ImageMobject(r'D:\DC\Desktop\LESManim\images\Gauss.jpg')

        diphantus.scale(0.8)
        kharezmi.scale(0.95)
        viete.scale(0.8)
        hals.scale(0.8)

        diphantusName = Text('Diophantos', font_size = 28, slant = ITALIC).next_to(diphantus, UP, buff = 0.2)
        diphantusDate = Text('350 n. Chr.', font_size = 18).next_to(diphantus, DOWN, buff = 0.2)
        kharezmiName = Text('al-Chwarizmi', font_size = 28, slant = ITALIC).next_to(kharezmi, UP, buff = 0.2)
        kharezmiDate = Text('780 - 850.', font_size = 18).next_to(kharezmi, DOWN, buff = 0.2)
        vieteName = Text('François Viète', font_size = 28, slant = ITALIC).next_to(viete, UP, buff = 0.2)
        vieteDate = Text('1540 - 1603.', font_size = 18).next_to(viete, DOWN, buff = 0.2)
        halsName = Text('René Descartes', font_size = 28, slant = ITALIC).next_to(hals, UP, buff = 0.25)
        halsDate = Text('1596 - 1650.', font_size = 18).next_to(hals, DOWN, buff = 0.2)
        gaussName = Text('Carl Friedrich Gauß', font_size = 28, slant = ITALIC).next_to(gauss, UP, buff = 0.25)
        gaussDate = Text('1777 - 1855.', font_size = 18).next_to(gauss, DOWN, buff = 0.2)
        

        heading_2 = Text('§1.Lineares Gleichung', font_size = 48, color = BLUE_B)


        gleichung = Text('Gleichheit, die einen unbekannten Wert, eine Variable, beinhaltet', font_size = 28, t2s = {'Variable':ITALIC})

        gleichungEG = MathTex(r"x+2=4", font_size = 78)
        gleichungEG2 = MathTex(r"2x-y=z", font_size = 78)
        gleichungEG3 = MathTex(r"ax+by=c", font_size = 78)

        gleichungEGClone = MathTex(r"x", r"+", r"2", r"=", r"4", font_size = 78).next_to(gleichungEG3, LEFT, buff=1.2)
        gleichungEG2Clone = MathTex(r"2", r"x", r"-", r"y", r"=", r"z", font_size = 78).next_to(gleichungEG3, RIGHT, buff=1.2)
        gleichungEG3Clone = MathTex(r"a", r"x", r"+", r"b", r"y", r"=", r"c", font_size = 78)

        gleichungGroup = VGroup(gleichungEG, gleichungEG2, gleichungEG3)
        gleichungGroupClone = VGroup(gleichungEGClone, gleichungEG2Clone, gleichungEG3Clone)
        why =  Text('?', font_size=384)

        x_power = MathTex(r"x^{1}", font_size=78).move_to(gleichungEGClone[0]).align_to(gleichungEGClone[0], DOWN).shift(0.15*RIGHT)
        

        x_power_2 = MathTex(r"x^{1}", font_size=78).move_to(gleichungEG2Clone[1]).align_to(gleichungEG2Clone[1], DOWN).shift(0.15*RIGHT)
        y_power_2 = MathTex(r"y^{1}", font_size=78).move_to(gleichungEG2Clone[3]).align_to(gleichungEG2Clone[3], DOWN).shift(0.15*RIGHT)
        
        x_power_3 = MathTex(r"x^{1}", font_size=78).move_to(gleichungEG3Clone[1]).align_to(gleichungEG3Clone[1], DOWN).shift(0.15*RIGHT)
        y_power_3 = MathTex(r"y^{1}", font_size=78).move_to(gleichungEG3Clone[4]).align_to(gleichungEG3Clone[4], DOWN).shift(0.15*RIGHT)
        
        gleichungEGClone2 = MathTex(r"x", r"+", r"2", r"y", r"^{0}", r"=", r"4", font_size = 78).next_to(gleichungEG3, LEFT, buff=0.8)
        gleichungEG2Clone2 = MathTex(r"2", r"x", r"-", r"y", r"=", r"z", font_size = 78).next_to(gleichungEG3, RIGHT, buff=0.8)
        gleichungEG3Clone2 = MathTex(r"a", r"x", r"+", r"b", r"y", r"=", r"c", font_size = 78)

        svoistvo1 = Text('1. Alle Variable haben Exponent nicht höher als 1',font_size = 28).shift(UP)
        svoistvo2 = Text('2. Es gibt immer 2 Variablen', font_size = 28)
        svoistvo3 = Text('3. Variable werden nicht miteinander multipliziert', font_size = 28).shift(DOWN)

        defenitionPT1 = Text("Gleichung ersten Grades,", font_size = 28, t2s = {'ersten Grades':ITALIC})
        defenitionPT2 = Text("bei der alle Variablen linear in die Gleichung eingehen", font_size = 28, t2s = {'linear':ITALIC}).next_to(defenitionPT1, DOWN)

        self.play(Write(heading_1))
        self.play(Write(names))
        self.play(Write(dateNplace))

        self.next_slide()

        self.play(FadeOut(heading_1, names, dateNplace))
        self.play(FadeIn(papyrus))
        self.play(Write(papyrusName))
    
        self.next_slide()

        self.play(FadeOut(papyrus, papyrusName))
        self.play(FadeIn(diphantus), Write(diphantusName), Write(diphantusDate))

        self.next_slide()

        self.play(FadeIn(kharezmi), Write(kharezmiName), Write(kharezmiDate))

        self.next_slide()

        self.play(FadeIn(viete), Write(vieteName), Write(vieteDate))

        self.next_slide()

        self.play(FadeIn(hals), Write(halsName), Write(halsDate))

        self.next_slide()

        self.play(FadeOut(diphantus, kharezmi, viete, hals, diphantusName, diphantusDate, kharezmiName, kharezmiDate, vieteName, vieteDate, halsName, halsDate))
        self.play(FadeIn(gauss), Write(gaussName), Write(gaussDate))

        self.next_slide()

        self.play(FadeOut(gauss), FadeOut(gaussName), FadeOut(gaussDate))
        self.play(Write(heading_2))

        self.next_slide()

        self.play(Transform(heading_2, gleichung))

        self.next_slide()

        self.play(FadeOut(heading_2))
        self.play(Write(gleichungEG))
        self.play(ApplyMethod(gleichungEG.next_to, gleichungEG3, LEFT, {"buff": 1.2}))

        self.next_slide()

        self.play(Write(gleichungEG2))
        self.play(ApplyMethod(gleichungEG2.next_to, gleichungEG3, RIGHT, {"buff": 1.2}))

        self.next_slide()

        self.play(Write(gleichungEG3))

        self.next_slide()

        self.play(ReplacementTransform(gleichungGroup, why))

        self.next_slide()

        self.play(ReplacementTransform(why, gleichungGroupClone))

        self.next_slide()

        self.play(Transform(gleichungEGClone[0], x_power))

        self.play(Transform(gleichungEG3Clone[1], x_power_3))
        self.play(Transform(gleichungEG3Clone[4], y_power_3))

        self.play(Transform(gleichungEG2Clone[1], x_power_2))
        self.play(Transform(gleichungEG2Clone[3], y_power_2))

        self.next_slide()

        self.play(ReplacementTransform(VGroup(gleichungEGClone, x_power), gleichungEGClone2), 
                  ReplacementTransform(VGroup(gleichungEG2Clone, x_power_2, y_power_2), gleichungEG2Clone2),
                  ReplacementTransform(VGroup(gleichungEG3Clone, x_power_3, y_power_3), gleichungEG3Clone2))
        
        self.play(FadeToColor(VGroup(gleichungEGClone2[0], gleichungEGClone2[3], gleichungEG2Clone2[1], gleichungEG2Clone2[3], gleichungEG3Clone2[1], gleichungEG3Clone2[4]), RED_E))

        self.next_slide()

        self.play(FadeOut(VGroup(gleichungEGClone2, gleichungEG2Clone2, gleichungEG3Clone2)))
        self.play(Write(svoistvo1))
        
        self.next_slide()

        self.play(Write(svoistvo2))

        self.next_slide()

        self.play(Write(svoistvo3))

        self.next_slide()

        title3 = Title("Lineare Gleichung", font_size=48)

        self.play(ReplacementTransform(VGroup(svoistvo1, svoistvo2, svoistvo3), VGroup(defenitionPT1, defenitionPT2)), DrawBorderThenFill(title3))

        self.next_slide()

        title = Title('Allgemeine Form', font_size=48)
        AllFormFormula = MathTex("a", "x",  "+",  "b", "y", "=", "c", font_size = 78)

        self.play(FadeOut(VGroup(defenitionPT1, defenitionPT2)), FadeOut(title3))
        self.play(DrawBorderThenFill(title), Write(AllFormFormula))

        self.next_slide()

        self.play(FadeToColor(VGroup(AllFormFormula[0],AllFormFormula[3], AllFormFormula[6]), GREEN_E))

        self.next_slide()

        self.play(FadeToColor(VGroup(AllFormFormula[1], AllFormFormula[4]), RED_E))

        self.next_slide()
        
        heading_3 = Text("§2. Lineares Gleichungssystem", font_size = 48, color = BLUE_B)

        self.play(FadeOut(VGroup(title, AllFormFormula)))
        self.play(Write(heading_3))

        self.next_slide()

        system1 = MathTex(r"\left\{ \begin{array}{cl} a_1x + b_1y = c_1 \\ a_2x + b_2y = c_2 \end{array} \right.", font_size = 78)
        system1_clone = MathTex(r"\left\{ \begin{array}{cl} a_1x + b_1y = c_1 \\ a_2x + b_2y = c_2 \end{array} \right.", font_size = 78)

        self.play(FadeOut(heading_3))
        self.play(Write(system1))

        self.next_slide()

        title = Title('Matrixschreibweise', font_size=48)
        system2 = MathTex(r"\begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} c_1\\ c_2 \end{pmatrix}", font_size = 78)

        self.play(DrawBorderThenFill(title), ReplacementTransform(system1, system2))

        self.next_slide()

        title2 = Title('Vektorschreibweise', font_size=48)
        system3 = MathTex(r"x \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} + y \begin{pmatrix} b_1 \\ b_2 \end{pmatrix} = \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}", font_size = 78)

        self.play(FadeOut(title))
        self.play(DrawBorderThenFill(title2), ReplacementTransform(system2, system3))

        self.next_slide()

        self.play(FadeOut(title2))
        self.play(ReplacementTransform(system3, system1_clone))

        self.next_slide()

        system4 = MathTex(r"\left\{ \begin{array}{cl} 2 + x = 4 \\ 10 - x = 8 \end{array} \right.", font_size=78)
        system4Done = MathTex(r"\left\{ \begin{array}{cl} 2 + 2 = 4 \\ 10 - 2 = 8 \end{array} \right.", font_size=78)
        xWhat = MathTex(r"x =", r"?", font_size = 78).to_corner(UL)
        xAnwser1 = MathTex(r"2", font_size = 78).move_to(xWhat[1]).shift(0.15*RIGHT)
    
        self.play(FadeOut(system1_clone))
        self.play(Write(system4))
        self.play(Write(xWhat))

        self.next_slide()

        self.play(ReplacementTransform(xWhat[1], xAnwser1),ReplacementTransform(system4, system4Done))

        self.next_slide()

        system5 = MathTex(r"\left\{ \begin{array}{cl}\ 6x - 8y = 13 \\ 6x + 9y = 6 \end{array} \right.", font_size = 78)

        self.play(FadeOut(xAnwser1, system4Done, xWhat))
        self.play(Write(system5))

        self.next_slide()

        self.play(FadeOut(system5))

        title4 = Title("Lösungsmethoden", font_size=48)

        method1 = Text("1. Eliminationsverfahren",font_size = 32).shift(UP)
        method2 = Text("2. Einsetzungsverfahren",font_size = 32).next_to(method1, DOWN)
        method3 = Text("3. Graphisches Verfahren",font_size = 32).next_to(method2, DOWN)
        method5 = Text("4. Gaußsches Eliminationsverfahren",font_size = 32).next_to(method3, DOWN)
        
        self.play(DrawBorderThenFill(title4))
        self.play(Write(method1))
        self.play(Write(method2))
        self.play(Write(method3))
        self.play(Write(method5))

        self.next_slide()

        title5 = Title("Eliminationsverfahren", font_size=48)
        xy = MathTex(r"(x = 1.8, y = 1.4)", font_size = 78)
        system6 = MathTex(r"\begin{cases} 2x + y = 5 \\ 3x - y = 4 \end{cases}", font_size = 78)
        system6Step1 = MathTex(r"2x+y = 5\\ 3x - y = 4 \\  \rule{1.9cm}{0.4pt} \\5x + 0 = 9 ", font_size = 78).move_to(ORIGIN)
        system6Step2 = MathTex(r"5x + 0 = 9", font_size = 78)
        system6Step3 = MathTex(r"5x = 9", font_size = 78)
        system6Step4 = MathTex(r"5x = 9 |\div5", font_size = 78)
        system6Step5 = MathTex(r"x = 1.8", font_size = 78)
        system6clone = MathTex(r"\begin{cases} 2\times1.8 + y = 5 \\ 3\times1.8 - y = 4 \end{cases}", font_size = 78)
        equations6 = MathTex(r"2\times1.8 + y = 5", font_size = 78)
        equations6_2 = MathTex(r"3.6 + y = 5", font_size = 78)
        equations6_3 = MathTex(r"y = 5 - 3.6", font_size = 78)
        equations6_4 = MathTex(r"y = 1.4", font_size = 78)
        system6FINAL = MathTex(r"\begin{cases} 2\times1.8 + 1.4 = 5 \\ 3\times1.8 - 1.4 = 4 \end{cases}", font_size = 78)

        
        
        self.play(FadeOut(VGroup(title4, method1, method2, method3, method5)))
        self.play(DrawBorderThenFill(title5))
        self.play(Write(system6))

        self.next_slide()

        self.play(FadeOut(system6))
        self.play(Write(system6Step1))

        self.next_slide()

        self.play(ReplacementTransform(system6Step1, system6Step2))

        self.next_slide()

        self.play(ReplacementTransform(system6Step2, system6Step3))
        
        self.next_slide()

        self.play(ReplacementTransform(system6Step3, system6Step4))

        self.next_slide()

        self.play(ReplacementTransform(system6Step4, system6Step5))

        self.next_slide()

        self.play(FadeOut(system6Step5))
        self.play(Write(system6clone))

        self.next_slide()

        self.play(FadeOut(system6clone))
        self.play(Write(equations6))

        self.next_slide()

        self.play(ReplacementTransform(equations6, equations6_2))

        self.next_slide()

        self.play(ReplacementTransform(equations6_2, equations6_3))

        self.next_slide()

        self.play(ReplacementTransform(equations6_3, equations6_4))

        self.next_slide()

        self.play(FadeOut(equations6_4))
        self.play(Write(xy))

        self.next_slide()

        self.play(FadeOut(xy))

        self.play(Write(system6FINAL))

        self.next_slide()

        title6 = Title("Einsetzungsverfahren", font_size=48)
        system7 = MathTex(r"\left\{ \begin{array}{cl} \ 6x - 8y  =  13 \\[1pt] 6x + 9y  =  6 \end{array} \right.", font_size = 78)
        system7step1 = MathTex(r"6x - 8y = 13", font_size = 78)
        system7step2 = MathTex(r"6x = 13 + 8y", font_size = 78)
        system7step3 = MathTex(r"6x + 9y = 6", font_size = 78)
        system7step4 = MathTex(r"13 + 8y + 9y = 6", font_size = 78)
        system7step5 = MathTex(r"13 + 17y = 6", font_size = 78)
        system7step6 = MathTex(r"17y = 6 - 13", font_size = 78)
        system7step7 = MathTex(r"17y = -7", font_size = 78)
        system7step8 = MathTex(r"17y = -7|\div17", font_size = 78)
        system7step9 = MathTex(r"y = \frac{-7}{17}", font_size = 78)
        system7step10 = MathTex(r"\left\{ \begin{array}{cl} \ 6x - 8\times\frac{-7}{17} = 13 \\[1pt] 6x + 9\times\frac{-7}{17} = 6 \end{array} \right.", font_size = 78)
        system7step11 = MathTex(r"6x = 13 + 8\times\frac{-7}{17}", font_size = 78)
        system7step12 = MathTex(r"6x = \frac{165}{17}", font_size = 78)
        system7step13 = MathTex(r"6x = \frac{165}{17}|\div6", font_size = 78)
        system7step14 = MathTex(r"x = \frac{55}{34}", font_size = 78)
        xy2 = MathTex(r"(x = \frac{55}{34}, y = \frac{-7}{17})", font_size = 78)
        system7FINAL = MathTex(r"\left\{ \begin{array}{cl} \ 6\times\frac{55}{34} - 8\times\frac{-7}{17} = 13 \\[2pt] 6\times\frac{55}{34} + 9\times\frac{-7}{17} = 6 \end{array} \right.", font_size = 78)


        self.play(FadeOut(VGroup(title5, system6FINAL)))

        self.play(DrawBorderThenFill(title6))
        self.play(Write(system7))

        self.next_slide()

        self.play(ReplacementTransform(system7, system7step1))

        self.next_slide()

        self.play(ReplacementTransform(system7step1, system7step2))

        self.next_slide()

        self.play(ApplyMethod(system7step2.shift, UP))
        self.play(Write(system7step3))

        self.next_slide()

        self.play(ReplacementTransform(VGroup(system7step2, system7step3), system7step4))

        self.next_slide()

        self.play(ReplacementTransform(system7step4, system7step5))

        self.next_slide()

        self.play(ReplacementTransform(system7step5, system7step6))

        self.next_slide()

        self.play(ReplacementTransform(system7step6, system7step7))

        self.next_slide()

        self.play(ReplacementTransform(system7step7, system7step8))

        self.next_slide()

        self.play(ReplacementTransform(system7step8, system7step9))

        self.next_slide()

        self.play(FadeOut(system7step9))
        self.play(Write(system7step10))

        self.next_slide()

        self.play(FadeOut(system7step10))
        self.play(Write(system7step11))

        self.next_slide()

        self.play(ReplacementTransform(system7step11, system7step12))

        self.next_slide()

        self.play(ReplacementTransform(system7step12, system7step13))

        self.next_slide()

        self.play(ReplacementTransform(system7step13, system7step14))

        self.next_slide()

        self.play(FadeOut(system7step14))
        self.play(Write(xy2))

        self.next_slide()

        self.play(FadeOut(xy2))
        self.play(Write(system7FINAL))

        self.next_slide()

        title7 = Title("Graphisches Verfahren" )
        system8 = MathTex(r"\left\{ \begin{array}{cl} \ 2x + y  =  5 \\[1pt] x - y  =  1 \end{array} \right.", font_size = 78)

        self.play(FadeOut(title6, system7FINAL))
        self.play(Write(title7))
        self.play(Write(system8))

        self.next_slide()

        ax = Axes(
            x_range=[-13, 13, 1],
            y_range=[-7, 7, 1],
            x_length=12 ,
            y_length=7,
        )

        def linear1(x):
            return 5-2*x
        
        def linear2(x):
            return x - 1
        
        graph1 = ax.plot(linear1, color=RED_E)
        graph2 = ax.plot(linear2, color=BLUE_E)
        
        point1 = Dot(ax.coords_to_point(2, 1))
        point1Label = MathTex("(2, 1)", font_size = 28).next_to(point1, RIGHT)
        system8COLOR = MathTex(r"\left\{ \begin{array}{cl} \ 2x + y = 5 \\[1pt] x - y = 1 \end{array} \right.", font_size=32).to_corner(UL)
        system8FINAL  = MathTex(r"\left\{ \begin{array}{cl} 4 + 1= 5 \\[1pt] 2 - 1 = 1 \end{array} \right.", font_size=32).to_corner(UL)

        self.play(FadeOut(system8, title7))
        self.play(Create(ax))
        self.play(Write(system8COLOR ))
        self.play(Create(graph1))
        self.play(Create(graph2))
        self.play(Create(point1))   
        self.play(Write(point1Label))     

        self.next_slide()
        
        self.play(ReplacementTransform(system8COLOR, system8FINAL))

        self.next_slide()

        def linear3(x):
            return 1-x
        
        def linear4(x):
            return 2-x
        
        graph3 = ax.plot(linear3, color=RED_E)
        graph4 = ax.plot(linear4, color=BLUE_E)
        
        system9 = MathTex(r"\left\{ \begin{array}{cl} x + y = 1 \\[1pt] \ 2x + 2y = 4 \end{array} \right.", font_size=32).to_corner(UL)
    
        self.play(Uncreate(VGroup(point1, system8FINAL, graph1, graph2, point1Label)))
        self.play(Write(system9))
        self.play(Create(graph3))
        self.play(Create(graph4))

        self.next_slide()

        def linear5(x):
            return 1-x
        
        def linear6(x):
            return 1-x
        
        graph5 = ax.plot(linear5, color=RED_E)
        graph6 = ax.plot(linear6, color=BLUE_E)
        
        system10 = MathTex(r"\left\{ \begin{array}{cl} \ x + y = 1 \\[1pt] 1 - y = x \end{array} \right.", font_size=32).to_corner(UL)

        self.play(Uncreate(VGroup(system9, graph3, graph1, graph4)))
        self.play(Write(system10))
        self.play(Create(graph5))
        self.play(Create(graph6))

        self.next_slide()

        self.play(FadeOut(system10, graph5, graph6, ax))

        self.next_slide()

        ty = Text("Viel Dank für hilfe").to_edge(UP)
        ty.set_color_by_gradient(BLUE_B)

        name2 = Text("Mokhamed Mansur", font_size=48, slant=ITALIC)
        name1 = Text("Kirilov Maxim", font_size=48, slant=ITALIC).next_to(name2, DOWN)
        name3 = Text("Losenko Pavel", font_size=48, slant=ITALIC).next_to(name2, UP)
        

        self.play(Write(ty))
        self.play(Write(name3))
        self.play(Write(name2))
        self.play(Write(name1))

        self.next_slide()

        ty4a = Text("Viel dank für ihre Aufmerksamkeit!", slant=ITALIC, font_size=48)

        self.play(FadeOut(ty, name3, name2, name1))
        self.play(Write(ty4a, run_time=6))

        self.next_slide()

        qrcode = ImageMobject(r'D:\DC\Desktop\LESManim\images\qr-code.png')
        qrcode.scale(0.3)

        self.play(FadeOut(ty4a))
        self.play(FadeIn(qrcode))


        






        