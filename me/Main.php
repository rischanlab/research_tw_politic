<?php


$file = "bio.txt";
$fh = fopen($file, 'a') or die("can't open file");
// set correct path!
require_once 'getAPI.php';
// change screen name to yours
$tw_account = array("alkwangju","kicaupemilu","rischanmafrur");
//echo "Total Followers : " . getTwitterFollowers($tw_account) . ", Total Friends : " . getTwitterFollowings($tw_account) ;
$tw_many = count($tw_account);

for($i=0; $i<$tw_many; $i++){
	$data = (getBio($tw_account[$i]));
		echo $data['name'] .",". $data['followers'] .",". $data['friends'] .",". $data['protected'] .",". $data['created_at'] .",". $data['favourites_count'] .",". $data['listed'] .",". $data['status'] .",". $data['location'] .",". $data['time_zone']  . "<br/>";
		fwrite($fh, $data['name'] .",". $data['followers'] .",". $data['friends'] .",". $data['protected'] .",". $data['created_at'] .",". $data['favourites_count'] .",". $data['listed'] .",". $data['status'] .",". $data['location'] .",". $data['time_zone']  . PHP_EOL);
}

fclose($fh);


// $data = getBio($tw_account);
// print_r($data);


?>