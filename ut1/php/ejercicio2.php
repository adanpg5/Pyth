<?	
$salario=$_POST["salario"];
$salario=(float)$salario;

$nombre=$_POST["nombre"];

$edad=$_POST["edad"];
$edad=(int)$edad;

	if ($salario >= 2000) {
    $salario = $salario;
}
	elseif (($salario >= 1000) and ($salario <= 2000)) {
    	if ($edad > 45) {
    		$salario = $salario + ($salario*0.03);
    	}
    	else {
    		$salario = $salario + ($salario*0.10);
    	}
    }
    elseif ($salario < 1000) {
    	if ($edad < 30) {
    		$salario = 1100;
    	}
    	elseif (($edad >= 30) and ($edad <= 45)) {
    		$salario = $salario + ($salario*0.03);
    	}
    	else {
    		$salario = $salario + ($salario*0.15);
    	}
    }
echo ("$nombre recibirá el siguiente salario: $salario")
?>
