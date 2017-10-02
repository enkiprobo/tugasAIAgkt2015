f(x1, x2 ) = (4 − 2,1x1<sup> 2</sup> + x1 <sup>4</sup>/ 3 ) x1 <sup>2</sup> + x1x2 + (−4 + 4x2 <sup>2</sup> )x2 <sup>2</sup>
<br><br><br>
<?php 
error_reporting(0);
function ex1($x1){
	$min = -10.0000000;
	$max = 10.0000000;
	
	$x1 = rand($min,$max);
	return $x1;
}

function ex2($x2){
	$min = -10.0000000;
	$max = 10.0000000;
	
	$x2 = rand($min,$max);
	return $x2;
}



for($i=0 ; $i < 100; $i++ ){
	$x1 = ex1($x1);
    $x2 =  ex2($x2);
	echo "f<sub>".$i."</sub>(x1, x2 ) =". $f[$i] = (4-2.1*pow($x1,2)+(pow($x1,4)/3))*pow($x1,2)+$x1*$x2+(-4+4*pow($x2,2))*pow($x2,2)." <br>"; 
}


echo "<br>Nilai terMinimum ". min($f);

?>

<br><br>
batasan −10 ≤ x1 ≤ 10 dan −10 ≤ x2 ≤ 10.
