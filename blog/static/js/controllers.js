var blogController = angular.module('blogControllers', [])

blogController.controller('IndexController', function($scope, $http){
    $http.get('/api/post').success(function(data){
        $scope.posts = data
    })
})

blogController.controller('NewPostController', function($scope, $http){
    $scope.formData = {}
    $scope.processForm = function(){
        $http.post('/api/post/', $scope.formData)
            .success(function(data){
                $scope.is_error = false
                $scope.submitted = true
                $scope.status = 'Your post was successfully saved!'
                $scope.formData = {}
            })
            .error(function(data){
                $scope.submitted = true
                $scope.is_error = true
                $scope.errors = data
            })
    }
})
