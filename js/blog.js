$(document).ready(function() {
    $("#enviar").click(function(){
        $.get("https://jsonplaceholder.typicode.com/posts/1/comments",
        function(data){
            console.log(data);
            $.each(data, function(i, item){
                $("#categoria").append('<div class="article"><div class="left"><img src="'+item.url+'"></img></div><div class="right"><p class="date">' + item.email + '</p><h1>' + item.name + '</h1><p class="description">' + item.body + '</p></div>');
            });
        });
    });
})