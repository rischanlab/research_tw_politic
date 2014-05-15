<?php

/** Just simple code for getting Bio twitter Account  **/
/** Rischan Mafrur  **/
/** April 28 2014   **/

$file = "bio.txt";
$fh = fopen($file, 'a') or die("can't open file");
// set correct path!
require_once 'getAPI.php';
// change screen name to yours
//$tw_account = array("alkwangju","kicaupemilu","rischanmafrur");
//echo "Total Followers : " . getTwitterFollowers($tw_account) . ", Total Friends : " . getTwitterFollowings($tw_account) ;
$tw_account = file('tw_input.txt',FILE_IGNORE_NEW_LINES);
//$tw_many = count($tw_account);
/*
foreach ($tw_account as $line_num => $line) {
    echo $line;
}
//*/
foreach($tw_account as $line_num => $line){

	$data = (getBio($line));
		echo $data['name'] .",". $data['followers'] .",". $data['friends'] .",". $data['protected'] .",". $data['created_at'] .",". $data['favourites_count'] .",". $data['listed'] .",". $data['status'] .",". $data['location'] .",". $data['time_zone']  . "<br/>";
		fwrite($fh, $data['name'] .",". $data['followers'] .",". $data['friends'] .",". $data['protected'] .",". $data['created_at'] .",". $data['favourites_count'] .",". $data['listed'] .",". $data['status'] .",". $data['location'] .",". $data['time_zone']  . PHP_EOL);
}

fclose($fh);


// $data = getBio($tw_account);
// print_r($data);


?>