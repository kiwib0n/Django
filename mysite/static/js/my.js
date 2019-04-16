
        var app = new Vue({
          el: '#app',
          data: {
            message: 'Привет, Vue!',
              seen: true,
              text: 'Спрятать',
              todos:[
                  {text: 'Изучить JavaScript', key:1},
                  {text: 'Изучить Vue', key:2},
                  {text: 'Изучить Python Django', key: 3},
              ],
              todoInput: '',

          },
            methods:{
              revers: function(){
                  this.message = this.message.split('').reverse().join('');
              },

                hide: function(){
                    (this.seen) ? this.seen = false : this.seen = true;
                    (!this.seen) ? this.text="Показать" : this.text="Спрятать";
                },

                addTodo: function(){
                    var inpt = document.getElementById("Todo");
                    var txt = inpt.value;
                    this.todos.push({text:txt, key:this.todos.length+1});
                    inpt.value = '';
                },

                /*
                   !!! Функция remove работает не корректно !!!
                */
                remove(key){
                  console.log(key);
                    side = [];

                    if( this.todos.length == 1)
                        this.todos.pop();

                    for(var i=0;i<this.todos.length;i++){
                        if(key == i+1)
                            continue;
                        else
                            side.push(this.todos[i]);
                    }
                    this.todos = side;
                }
            },
        });