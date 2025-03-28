import flet as ft

def main(page: ft.Page):
    page.title = 'App'

    task_field = ft.TextField(hint_text='Write a task...', expand=True)
    task_list = ft.Column()

    def add_task(e):
        if task_field.value:
            task = ft.Row(
                [
                    ft.Text(task_field.value, expand=True),
                    ft.IconButton(ft.icons.DELETE, icon_color='#fc0303',on_click=lambda e:remove_task(e, task))
                ]
            )
            task_list.controls.append(task)
            task_field.value = ''
            page.update()
    def remove_task(e, task):
        task_list.controls.remove(task)
        page.update()
    page.add(
         ft.Row([
             task_field, ft.ElevatedButton(ft.icons.ADD, on_click=add_task)
         ]),
         task_list
    )
ft.app(main)
