import flet as ft

def main(page:ft.Page):
    page.window.always_on_top=True
    page.title="To_Do Application(1st Project: 23.Nov.2025)"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
     
    a=ft.IconButton(icon=ft.Icons.SUNNY,on_click= lambda _: theme())
    appbar=ft.AppBar(
        leading=None,
        title=ft.Text(
              value="To_Do App",
              weight=ft.FontWeight.BOLD,
              color=ft.Colors.BLUE,
            ),
        center_title=True,
        actions=[
            a
        ]
    )
    

    def theme():
        if a.icon==ft.Icons.SUNNY:
            a.icon=ft.Icons.DARK_MODE
            page.theme_mode=ft.ThemeMode.DARK
        else:
            a.icon=ft.Icons.SUNNY
            page.theme_mode=ft.ThemeMode.LIGHT

        page.update()



    # method to return task and status
    def create_new_task(text):
        #Status dropdown which shows active,pending, completed
        status=ft.Dropdown(
            value="Active",
            options=[
                ft.DropdownOption(text="Active",),
                ft.DropdownOption(text="Pending"),
                ft.DropdownOption(text="Completed")
            ],
            on_change= lambda _: Status_update_method(status),
            width=150
          )
        Status_update_method(status)

        task_row = ft.Row(
            controls=[
                ft.Text(text, expand=True),
                status,
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color=ft.Colors.RED,
                    on_click=lambda e: delete_task(task_row),
                ),
            ]
        )

        return task_row

    #method for deleting a task
    def delete_task(row):
        tasks.controls.remove(row)
        page.update()


    #method for task to be added
    def task_add_method():
        print("Clicked")
        if NewTask.value=="":
            print("No task Added")
            return
        
        tasks.controls.append(create_new_task(NewTask.value))
        NewTask.value=""
        page.update()



    #method to update status
    def Status_update_method(s):
        print("Clicked")

        if s.value=="Active":
            s.color=ft.Colors.GREEN
        elif s.value=="Pending":
            s.color=ft.Colors.RED_900
        elif s.value=="Completed":
            s.color=ft.Colors.BLUE
        page.update()


    #textfield for new Task
    NewTask=ft.TextField(
        label="New Task",
        expand=True,
        multiline=True,
        shift_enter=True,
        on_submit= lambda _: task_add_method()
        )
    

    #add button which triggers task_add_method()
    AddButton=ft.ElevatedButton(
        text="Add Task",
        on_click= lambda _: task_add_method(),
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
        
    )
    

    tasks=ft.Column(
        controls=[],
        
        )
    
    btmBar=ft.BottomAppBar(
        content=ft.Text("Made by Maryam Nazar",text_align=ft.TextAlign.CENTER)
    )

    page.add(appbar,
             ft.Row(
                 controls=[NewTask,AddButton]
                 ),
            ft.Container(
                content=tasks,padding=10
                
                ),
            btmBar

            )

ft.app(main)