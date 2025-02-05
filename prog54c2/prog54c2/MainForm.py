import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(22, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(151, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Raidus:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(22, 57)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(151, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Area:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(22, 102)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(151, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Circumference:"
		self._label3.Click += self.Label3Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 142)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 56)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(118, 142)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 56)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(224, 142)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 56)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(198, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 31)
		self._textBox1.TabIndex = 6
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(198, 57)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 7
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(198, 102)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(332, 207)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog54c2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pi = (3.14159)
		radius = float(self._textBox1.Text)
		circ = 2 * pi * radius
		area = pi * (radius**2)
		self._label4.Text = str(round(area, 3))
		self._label5.Text = str(round(circ, 3))
		

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._label5.Text = ""
		self._textBox.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label3Click(self, sender, e):
		pass