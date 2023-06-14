from flet import *

def main(page:Page):
	page.window_width=300
	page.padding=0
	page.spacing=0

	def youchangechoince(e):
		# AND NOW I WILL GET NAME AND INDEX YOU SELECT 
		# IN TABS
		youindex = e.control.selected_index
		namescreen = e.control.tabs[youindex].text
		for x in range(0,len(e.control.tabs)):
			if youindex == x:
				# AND SET SCREEN NAME 
				page.controls[0].controls[0].content.controls[0].value = namescreen
		page.update()


	# AND NOW CREATE TABS
	mytab = Tabs(
		selected_index=0,
		animation_duration=300,
		unselected_label_color="black",
		label_color="white",
		indicator_color="white",
		indicator_border_radius=30,
		divider_color="#7c59f0",
		# AND ACTIVATE SCROLL
		scrollable=True,
		on_change=youchangechoince,
		tabs=[
			Tab(
				text="Home",
				icon="home"
				),
			Tab(
				text="Face",
				icon="face"
				),
			Tab(
				text="person",
				icon="person"
				),
			Tab(
				text="notifications",
				icon="notification_add"
				),
		]
		)


	mybar = Container(
		border_radius=border_radius.vertical(
			bottom=30
			),
		# ADD SHADOW TO CONTAINER
		shadow=BoxShadow(
			spread_radius=1,
			blur_radius=10,
			color="#fc4795",
			),
			gradient=LinearGradient(
				begin=alignment.top_left,
				end=alignment.bottom_right,
				colors=["#fc4795","#7c59f0"]
				),
			width=page.window_width,
			height=150,
			padding=10,
			content=Column([
				Row([
					IconButton(icon="menu",
					icon_size=25,
					icon_color="white"
						),
					Text("Flet App",size=25,color="white",
						weight="bold"
						),
					Row([
						IconButton(icon="notifications",
					icon_size=25,
					icon_color="white"
						),
						IconButton(icon="search",
					icon_size=25,
					icon_color="white"
						),
						])
					],alignment="spaceBetween"),
				mytab
				])
			
		)
	page.overlay.append(mybar)
	page.add(
		Column([
			Container(
				margin=margin.only(
					top=page.window_height/2,
					),
				alignment=alignment.center,
				content=Column([
					Text("Sample",size=30)
					])
				)
			])
		)

flet.app(target=main)
