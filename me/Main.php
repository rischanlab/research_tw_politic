<?php

// set correct path!
require_once 'getAPI.php';
// change screen name to yours
$tw_account = array("alkwangju","kicaupemilu","rischanmafrur");
//echo "Total Followers : " . getTwitterFollowers($tw_account) . ", Total Friends : " . getTwitterFollowings($tw_account) ;
$tw_many = count($tw_account);

for($i=0; $i<$tw_many; $i++){
	print_r(getBio($tw_account[$i]));
	
}

// $data = getBio($tw_account);
// print_r($data);


?>