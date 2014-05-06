#!/bin/perl -w

#Perl script for processing a geometry form
#Kyle Hughes   HW #5
use strict;
use CGI qw/:standard/;
use Scalar::Util qw(looks_like_number);
my($height,$width,$radius,$info,$shape);
print header,
	start_html(-title =>'Geometry Form', -style 
	
=>['/~hughes72/web/hw2/normal.css','/~hughes72/web/hw2/webline.css']),

 	"<div id = \"head\">",
	h1('Geometry Form'),
	"</div>","<div id = \"wrapper1\">",
	start_form,
	"<fieldset> <label><b>Shape: </b></label>",

	popup_menu(-name=>'shape', -values=>
	['Rectangle','Circle','Right Triangle','Isosceles Triangle']),
	"</fieldset>",
	"<fieldset> <label><b> Data:</b> </label>",hr,p,"\n\n",
	"Radius:",textfield('radius'),p,
	"Height:",textfield('height'),p,
	"Width:",textfield('width'),p,
	"</fieldset>",
	"<fieldset> <label><b> Important Info</b>: </label>",hr,p,
		
radio_group(-name=>'info',values=>['Area','Perimeter'],),
"</fieldset>",p,hr,submit,defaults('Reset'),end_form,hr;
if(param()){
my($answer);
$width= param('width');
$height= param('height');

$radius= param('radius');
$info= param('info');
$shape= param('shape');
	if($shape eq "Circle"){
	if(looks_like_number($radius)){
	      if($info eq "Area"){
                         $answer = 3.14 * $radius**2;}
                         else{
                                 $answer = 3.14 *(2 *$radius);}
                         print "The $info of this $shape with radius
                         $radius is $answer";
			
                 }
	else{	print"Enter a real radius";}
}
else{
	if(looks_like_number($width)){
		if(looks_like_number($height)){

	
	if($shape eq "Rectangle"){
		
		if($info eq "Area"){
			$answer = $height * $width;}
			
		else{
			$answer = (2*$height) + (2*$width);
			}	
			print "The $info of this $width by $height $shape 
			is $answer";
			print' <img src="rectangle.svg" alt=""/>';
}
		if($shape eq "Right Triangle"){
			if($info eq "Area"){
				$answer = ($height *$width) /2;
			}
			else{
				my $temp = ($height**2 +$width**2)**0.5;
				$answer = $height + $width +$temp;}
			print "The $info of this $width by $height $shape 
			is $answer";
		}
		if($shape eq "Isosceles Triangle"){
			if($info eq "Area"){
				$answer = ($width*$height)/2;
			print "The $info of this $width by $height $shape 
			is $answer";}
			
				elsif($info eq "Perimeter"){
			print "You can not find the $info of this $shape
			with the given Data";}
}


		 
}
else{	if($shape eq "Circle"){
		if(looks_like_number($radius)){
		      if($info eq "Area"){
                         $answer = 3.14 * $radius**2;}
                         else{
                                 $answer = 3.14 *(2 *$radius);}
                         print "The $info of this $shape with radius
                         $radius is $answer";
                 }
		else{ print "Enter a real radius";}

	}
		
else{print "Enter a real number for Height please";}



}
}
else{
if($shape eq "Circle"){    	
if(looks_like_number($radius)){
	
                         if($info eq "Area"){
                         $answer = 3.14 * $radius**2;}
                         else{
                                 $answer = 3.14 *(2 *$radius);}
                         print "The $info of this $shape with radius
                         $radius is $answer";
                 }
	
	else{print "Enter a real radius please";
	}
 }

else{ if(looks_like_number($height)){
	print "Enter a real number for Width please";}
	else{
	print "Enter numbers for Height and Width";}

}
}
}

}
print "</div>";

print" <div id = \"bottom\">


<table id=\"webline\">
	<tr>
	<td style=\"word-spacing:1em;\">Valid:
	<a href=\"http://validator.w3.org/check/referer\">HTML5</a>
	<a 
href=\"http://jigsaw.w3.org/css-validator/check/referer?profile=css3\">CSS</a>
	</td>

	<td style=\"word-spacing:1em;\">Tests:
	<a href=\"Ishot.png\">IE</a>
	<a href=\"Foxshot.png\">Mozilla</a>
	<a href=\"Safshot.png\">Safari</a>
	<a href=\"Oshot.png\">Opera</a>
	<a href=\"Wshot.png\">W3M</a>
	<a href=\"Lshot.png\">Lynx</a>
	</td>

	</tr>
	</table>
	</div>
                    




								
	       				";
print end_html();
