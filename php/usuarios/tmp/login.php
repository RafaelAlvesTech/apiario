<?php 

include_once("../conexao.php");

/*setlocale(LC_ALL,'pt_BR.UTF8');
mb_internal_encoding('UTF8'); 
mb_regex_encoding('UTF8');
*/
$usuario = $_GET['usuario'];
$senha = $_GET['senha'];



$dados = array();


$query = $pdo->query("SELECT fun_id = fun_id, fun_login = ltrim(rtrim(fun_login)), fun_senha = ltrim(rtrim(fun_senha)), fun_nm = ltrim(rtrim(fun_nm)) from tab_fun where ltrim(rtrim(fun_login)) = '$usuario' ");

//$query = $pdo->query("SELECT * from tab_fun where fun_login = '$usuario' and fun_senha = '$senha'");
$res = $query->fetchAll(PDO::FETCH_ASSOC);

for ($i=0; $i < count($res); $i++) { 
      foreach ($res[$i] as $key => $value) {}

      	$dados = $res;


}

echo ($res) ?
json_encode(array("code" => 1, "result"=>$dados)) : 
json_encode(array("code" => 0, "message"=>"Dados incorretos!")) 



?>