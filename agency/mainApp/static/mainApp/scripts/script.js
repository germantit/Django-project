function viewHouseCard(i){
    i--;
    document.getElementsByClassName('house-card')[i].style.display = "block";
    $('body').not(this).css('pointer-events', 'none');
};

function closeHouseCard(i){
    i--;
    document.getElementsByClassName("house-card")[i].style.display = "none";
    $('body').css('pointer-events', 'auto');
};

function viewHousePlan(i){
    i--;
    document.getElementsByClassName('house-plan')[i].style.display = "block";
};

function closeHousePlan(i){
    i--;
    document.getElementsByClassName("house-plan")[i].style.display = "none";
    $('body').not(this).css('pointer-events', 'auto');
};


function backToTop() {
    let button = $('.back-to-top');

    $(window).on('scroll', () => {
        if($(this).scrollTop() >= 50) {
            button.fadeIn();
        } else {
            button.fadeOut();
        }
    });

    button.on('click', (e) => {
        e.preventDefault();
        $('html').animate({scrollTop: 0}, 1000);
    })
}

backToTop();


$(document).ready(function() {
	$(".fancybox").fancybox({
		openEffect	: 'none',
		closeEffect	: 'none'
	});
});
