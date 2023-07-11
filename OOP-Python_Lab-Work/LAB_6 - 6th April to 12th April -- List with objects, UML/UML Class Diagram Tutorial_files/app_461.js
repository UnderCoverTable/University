$(document).ready(function(){var switched=false;var updateTables=function(){if(($(window).width()<900)&&!switched){switched=true;$("table.responsive").each(function(i,element){splitTable($(element));});return true;}
else if(switched&&($(window).width()>900)){switched=false;$("table.responsive").each(function(i,element){unsplitTable($(element));});}};$(window).load(updateTables);$(window).bind("resize",updateTables);function splitTable(original)
{original.wrap("<div class='table-wrapper' />");var copy=original.clone();copy.find("td:not(:first-child), th:not(:first-child)").css("display","none");copy.removeClass("responsive");original.closest(".table-wrapper").append(copy);copy.wrap("<div class='pinned' />");original.wrap("<div class='scrollable' />");}
function unsplitTable(original){original.closest(".table-wrapper").find(".pinned").remove();original.unwrap();original.unwrap();}});


$(document).foundation();
$('.title-bar').on('sticky.zf.stuckto:top', function(){
	$(this).addClass('shrink');
});
$('.title-bar').on('sticky.zf.unstuckfrom:top', function(){
	$(this).removeClass('shrink');
});

$('.tut-bar').on('sticky.zf.stuckto:top', function(){
	$(this).addClass('shrink');
});
$('.tut-bar').on('sticky.zf.unstuckfrom:top', function(){
	$(this).removeClass('shrink');
});

$(".off-canvas").on("opened.zf.offcanvas", function() {
	  $('html,body').css('overflow-y', 'hidden');
});
$(".off-canvas").on("closed.zf.offcanvas", function() {
	  $('html,body').css('overflow-y', '');
});

var lIsMSIE = false;
$(function(){

    // Attach the change event listener to change the label of all input[type=file] elements
    var els = document.querySelectorAll("input[type=file]"),
        i;
    for (i = 0; i < els.length; i++) {
        els[i].addEventListener("change", function() {
            var label = this.previousElementSibling;
            label.innerHTML = this.files[0].name;
        });
    }

    try {
    	var ua = window.navigator.userAgent;
    	lIsMSIE = ua.indexOf('MSIE ')>0;
    } catch (e) {}

    // scroll to top
	$(document).on( 'scroll', function(){
		if ($(window).scrollTop() > 100) {
			$('.scroll-top-wrapper').addClass('show');
		} else {
			$('.scroll-top-wrapper').removeClass('show');
		}
	});
	$('.scroll-top-wrapper').on('click', scrollToTop);
	
	// defer load css
	if (lDeferStyleSheets) {
		lDeferStyleSheets.forEach(function(css) {
			loadStyleSheet(css);
		});
	}
});
 
function scrollToTop() {
	verticalOffset = typeof(verticalOffset) != 'undefined' ? verticalOffset : 0;
	element = $('body');
	offset = element.offset();
	offsetTop = offset.top;
	$('html, body').animate({scrollTop: offsetTop}, 500, 'linear');
}

function getTimeZone() {
	var tzo=(new Date().getTimezoneOffset()/60)*(-1);
	var prefix = "GMT ";
	if (tzo >= 0) {
  	prefix += "+";
	}
	tzo = prefix + tzo;
	return tzo;
}
function setCookie(name, value, expires, path, domain, secure) {
	if (expires==undefined) {
		expires = new Date(new Date().getTime() + (1000*60*60*24 *90));
	}
	if (path==undefined) {
		path = "/";
	}
    document.cookie= name + "=" + escape(value) +
        ((expires) ? "; expires=" + expires.toGMTString() : "") +
        ((path) ? "; path=" + path : "") +
        ((domain) ? "; domain=" + domain : "") +
        ((secure) ? "; secure" : "");
}

function getCookie(name) {
    var dc = document.cookie;
    var prefix = name + "=";
    var begin = dc.indexOf("; " + prefix);
    if (begin == -1) {
        begin = dc.indexOf(prefix);
        if (begin != 0) return null;
    }
    else { begin += 2; }
    var end = document.cookie.indexOf(";", begin);
    if (end == -1) { end = dc.length; }
    return unescape(dc.substring(begin + prefix.length, end));
}

function removeCookie(name) {
	var date = new Date();
	date.setTime(date.getTime()+(-1*24*60*60*1000));
	setCookie(name, "", date, "/");
}
function getEditionName(aEditionCode) {
	if ('ee'==aEditionCode) {
		return 'Enterprise';
	} else if ('pe'==aEditionCode) {
		return 'Professional';
	} else if ('se'==aEditionCode) {
		return 'Standard';
	} else if ('me'==aEditionCode) {
		return 'Modeler';
	} else if ('ce'==aEditionCode) {
		return 'Community';
	} else if ('pr'==aEditionCode) {
		return 'Premium';
	} else if ('es'==aEditionCode) {
		return 'Essential';
	} else if ('ad'==aEditionCode) {
		return 'Advance';
	} else if ('st'==aEditionCode) {
		return 'Starter';
	} else if ('ex'==aEditionCode) {
		return 'Express';
	} else {
		return '';
	}
}

function refreshCaptcha() {
	var img = document.getElementById("jc_captchaImg");
	var path = "/servlet/captcha?rand="+randomStr(4);
	img.src = path;
}
var chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
function randomStr(len) {
	var result = "";
	for (var i=0;i<len;i++) {
		result += chars.charAt(Math.random()*chars.length);
	}
	return result;
}

function loadStyleSheet(src) {
    if (document.createStyleSheet){
        document.createStyleSheet(src);
    }
    else {
        $("head").append($("<link rel='stylesheet' href='"+src+"' type='text/css' />"));
    }
};

Foundation.Abide.defaults.patterns['letters_num_and_spaces'] = /^[\w\-\s\!\$&'\(\)\*\+,:;=./#%?^"]+$/;
Foundation.Abide.defaults.patterns['letters_and_spaces'] = /^[A-Za-z\-\s]+$/;


Foundation.onImagesLoaded = function(images, callback) {
    var self = this,
        unloaded = images.length;

    if (unloaded === 0) {
      callback();
    }

    images.each(function () {
      // Check if image is loaded
      if (this.complete || this.readyState === 4 || this.readyState === 'complete') {
        singleImageLoaded();
      }
      // Force load the image
      else {
          // fix for IE. See https://css-tricks.com/snippets/jquery/fixing-load-in-ie-for-cached-images/
    	  if (lIsMSIE) {
            var src = $(this).attr('src');
            $(this).attr('src', src + (src.indexOf('?') >= 0 ? '&' : '?') + new Date().getTime());
    	  }
          $(this).one('load', function () {
            singleImageLoaded();
          });
        }
    });

    function singleImageLoaded() {
      unloaded--;
      if (unloaded === 0) {
        callback();
      }
    }
};
