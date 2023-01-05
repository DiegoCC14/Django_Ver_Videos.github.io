$(document).ready(function(){
    //let videos_json = [{"nombre":"Diego"},{"nombre":"Cazon"}]
    //pinta_datos_video(videos_json)
    console.log("Comienzo!!!")
    obtener_info_videos( pinta_datos_video_usuario )
    obtiene_infor_top_videos( pinta_datos_top_videos_publicos )
    console.log("Final!!!")
})

function pinta_datos_video_usuario( json_video ){
    json_video.forEach( video => {
        let div_article = $("#div_article_main").clone()
        $(div_article).attr("hidden",false)

        $(div_article).find("h2").text( video["titulo"] )
        $(div_article).find(".published").text( video["fecha_ingreso"] )
        $(div_article).find(".author").text( "User123" )
        //$(div_article).find("#image_video_user").attr("src","second.jpg")
        $( div_article ).insertBefore("#div_article_main")
        //$("#main").append( div_article , 0 )
    }); 
}

function pinta_datos_top_videos_publicos( json_video ){
    json_video.forEach( video => {
        let div_mini_article = $("#div_article_section").clone()
        $(div_mini_article).attr("hidden",false)

        $(div_mini_article).find("h3").text( video["titulo"] )
        $(div_mini_article).find(".published").text( video["fecha_ingreso"] )
        $(div_mini_article).find(".author").text( "User12345" )
        //$(div_article).find("#image_video_user").attr("src","second.jpg")
        $( div_mini_article ).insertBefore("#div_article_section")
        //$("#main").append( div_article , 0 )
    }); 
}

function obtener_info_videos( function_pinta_datos ){
    $.ajax({
        url:'/app/api_videos/',
        type:'get',
        data:{
            "limite_inferior":0,
            "limite_superior":4
        },
        dataType:'JSON',
        success: function( request ){
            console.log( request )
            function_pinta_datos( request["videos_user"] )
        },
        error: function( request ){
            console.log("Error 123")
        },
    })
}

function obtiene_infor_top_videos( function_pinta_datos ){
    $.ajax({
        url:'/app/api_top_videos/',
        type:'get',
        data:{
            "limite_inferior":0,
            "limite_superior":2
        },
        dataType:'JSON',
        success: function( request ){
            console.log( request )
            function_pinta_datos( request["top_videos"] )
        },
        error: function( request ){
            console.log("Error 123")
        },
    })
}