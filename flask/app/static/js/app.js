$(document).ready(function () {

    // Jquery for the trend list group
    $('.list-group-item').on('click', function () {
        // console.log('here!');
        var $this = $(this);
        var $alias = $this.data('alias');

        $('.list-group > .list-group-item').removeClass('active');
        $this.toggleClass('active');

        // Pass clicked link element to another function
        switchTrend($this, $alias);
    });

    $(".btn-group > .btn").click(function(){
        console.log('here')
        $(this).addClass("active").siblings().removeClass("active");
        $(this).blur();
    });
});

function switchTrend($this, $alias) {
    console.log($this.text());  // Will log Paris | France | etc...

    console.log($alias);  // Will output whatever is in data-alias=""
}

function switchNutritionalView($this, $alias) {
    console.log($this.text());  // Will log Paris | France | etc...

    console.log($alias);  // Will output whatever is in data-alias=""
}