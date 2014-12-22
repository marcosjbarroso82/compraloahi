/**
 * AdCtrl
 * @namespace dashBoardApp.ad.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.controllers')
        .controller('AdCtrl', AdCtrl);

    AdCtrl.$inject = ['$scope', 'Ad', 'Snackbar'];

    /**
     * @namespace AdCtrl
     */
    function AdCtrl($scope, Ad, Snackbar) {
        $scope.ads = {};
        $scope.next_page = null;
        $scope.prev_page = null;
        $scope.count_page = 0;
        $scope.current_page = 1;
        $scope.pages = [];

        getAds();

        function getAds(){
            Ad.get(function(data) {
                $scope.ads = data.results;
                $scope.count_page = parseInt(data.count/5) + 1;
                for(var i=1; i <= $scope.count_page; i++){
                    $scope.pages.push(i);
                }
                $scope.next_page = data.next;
                $scope.prev_page = data.previous;

                if($scope.next_page){
                    $scope.next = false;
                }else{
                    $scope.next = true;
                }

                if($scope.prev_page){
                    $scope.prev = false;
                }else{
                   $scope.prev = true;
                }
            });
        }

        $scope.get_ads_page = function(page){
            Ad.get({"page":page},function(response) {
                $scope.current_page = page;
                $scope.ads = response.results;
                $scope.next_page = response.next;
                $scope.prev_page = response.previous;
            });
        };

        $scope.changePage = function(){
            console.log("CAMBIO DE PAGINA! ");
        };



        $scope.submitAd= function(text) {
            var ad = new Ad({text: text});
            ad.$save(function(){
                $scope.ads.unshift(ad);
            })
        };
        $scope.deleteAd= function(ad) {

            Ad.delete({id:ad.id}, deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                getAds();
                //$scope.ads.splice($scope.ads.indexOf(ad),1);
                Snackbar.show("El aviso fue eliminado con exito!");
            }

            function deleteError(data, headers, status){
                Snackbar.error("Error al intentar borrar el aviso");
            }
        };


    }
})();