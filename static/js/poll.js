var app = angular.module('polApp', []);

app.controller('pollCtrl', function($scope, $http) {

  //GET VALUES FROM A JSON FILE
  /*
  $http.get('poll.json').then(function(response){
    $scope.test = response.data;
    $scope.yes = $scope.test[0].yes_votes;
    $scope.no = $scope.test[0].no_votes;
    $scope.total = $scope.yes + $scope.no;
    $scope.yesPer = Math.round(100 *($scope.yes/$scope.total)) ;
    $scope.noPer = Math.round(100 *($scope.no/$scope.total)) ;

  });
*/

  //set this values to empty if getting data from A JSON file.
  $scope.answered = false;
  $scope.yes = 10;
  $scope.no = 20;
  $scope.total = $scope.yes + $scope.no;
  $scope.yesPer = Math.round(100 * ($scope.yes / $scope.total));
  $scope.noPer = Math.round(100 * ($scope.no / $scope.total));

  $scope.addYes = function() {
    $scope.yes = $scope.yes + 1;
    $scope.total = $scope.yes + $scope.no;
    $scope.yesPer = Math.round(100 * ($scope.yes / $scope.total));
    $scope.noPer = Math.round(100 * ($scope.no / $scope.total));
  }
  $scope.addNo = function() {
    $scope.no = $scope.no + 1;
    $scope.total = $scope.yes + $scope.no;
    $scope.yesPer = Math.round(100 * ($scope.yes / $scope.total));
    $scope.noPer = Math.round(100 * ($scope.no / $scope.total));
  }

});
