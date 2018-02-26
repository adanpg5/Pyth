<!doctype html>
<html lang="es">
	<head>
		<meta charset="utf-8">
		<title>Tablas</title>
	</head>
	<body>
		<h1>¡Haz tu tabla!</h1>
		<form action="ejercicio4.php" method="get">
			<label for="filas">¿Cuántas filas quieres?</label>
			<input type="text" name="filas"/><br>
			<label for="colum">¿Cuántas columnas quieres?</label>
			<input type="text" name="colum"/><br>
			<input type="submit" value="enviar"/>
		</form>
		<br>
		<?php
			if ((isset($_GET["filas"]) and isset($_GET["colum"]))) {
				$filas = (int)$_GET["filas"];
				$colum = (int)$_GET["colum"];
				if ($filas < 1 or $colum < 1) {
					echo("<p style='color:blue;'>Mínimo 1 columna y 1 fila.</p>");
				}
				else {
					echo("<table border='1'>");
					for($i=1; $i<=$filas; $i++){
						echo("<tr>");
						for($j=1; $j<=$colum; $j++){
							echo("<td>xd</td>");
						}
						echo("</tr>");
					}
					echo("</table>");
				}
			}
		?>
	</body>
</html>