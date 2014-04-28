<?php

// set correct path!
require_once 'getAPI.php';
// change screen name to yours
$tw_account ="kicaupemilu";
//echo "Total Followers : " . getTwitterFollowers($tw_account) . ", Total Friends : " . getTwitterFollowings($tw_account) ;
$data = getBio($tw_account);
print_r($data);


?>