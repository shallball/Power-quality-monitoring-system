# coding=gbk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import account as acc
import save,frame


def change_admin(self):
	self.destroy()
	acc.account_login()


def about():
	root=Tk()
	root.resizable(0,0)
	root.title('����')
	Label(root,text='���ߣ��ƿ�').grid(padx=10,pady=10,sticky=W)
	Label(root,text='���䣺1132970244@qq.com').grid(padx=10,pady=10,sticky=W)
	ttk.Button(root,text='ȷ��',command=root.destroy).grid(padx=10,pady=10)
	root.mainloop()
		
def makemenu(win):
	global flag_save
	flag_save=0
	top=Menu(win)
	win.config(menu=top)
	sys=Menu(top,tearoff=False)
	sys.add_command(label='�л��û�',
	command=lambda:change_admin(win),underline=0)
	top.add_cascade(label='ϵͳ',menu=sys,underline=0)
	
	analysis=Menu(top,tearoff=False)
	analysis.add_command(label='��ѹ��Ƶ��ƫ��',
	command=lambda:frame.switch(8),underline=0)
	analysis.add_command(label='г������',
	command=lambda:frame.switch(9),underline=0)
	analysis.add_command(label='���಻ƽ��',
	command=lambda:frame.switch(10),underline=0)
	top.add_cascade(label='����������ʾ',menu=analysis,underline=0)
	
	view=Menu(top,tearoff=False)
	view.add_command(label='A����Чֵ����ͼ',
	command=lambda:frame.switch(0),underline=0)
	view.add_command(label='B����Чֵ����ͼ',
	command=lambda:frame.switch(1),underline=0)
	view.add_command(label='C����Чֵ����ͼ',
	command=lambda:frame.switch(2),underline=0)
	view.add_command(label='A��˲ʱֵ����ͼ',
	command=lambda:frame.switch(3),underline=0)
	view.add_command(label='B��˲ʱֵ����ͼ',
	command=lambda:frame.switch(4),underline=0)
	view.add_command(label='C��˲ʱֵ����ͼ',
	command=lambda:frame.switch(5),underline=0)
	view.add_command(label='������ѹ���ݱ�  ',
	command=lambda:frame.switch(6),underline=0)
	view.add_command(label='���๦�����ݱ�  ',
	command=lambda:frame.switch(7),underline=0)
	top.add_cascade(label='����������ʾ',menu=view,underline=0)

	
	tool=Menu(top,tearoff=False)
	tool.add_command(label='��ʼ��¼',
	command=save.save_start,underline=0)
	tool.add_command(label='������¼',
	command=save.save_stop,underline=0)
	tool.add_command(label='��ʷ���ݲ�ѯ',
	command=save.save_window,underline=0)
	top.add_cascade(label='���ݼ�¼',menu=tool,underline=0)
	

	help=Menu(top,tearoff=False)
	help.add_command(label='����',command=about,underline=0)
	top.add_cascade(label='����',menu=help,underline=0)


	

