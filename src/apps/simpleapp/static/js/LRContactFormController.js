app.controller('LRContactFormController', ['$scope', '$http', 'vcRecaptchaService', function($scope, $http, vcRecaptchaService) {
    $scope.submit = function(parameters) {
        parameters['g-recaptcha-response'] = vcRecaptchaService.getResponse();
        $http.post('api/feedback/', parameters)
            .success(function(response) {
                if (response['status']) {
                    console.log('Form success.');
                    $scope.form_hide = true;
                    $scope.status_message = 'Form successfully submited.';
                } else {
                    console.log('Error while verifying captcha on server');                    
                    $scope.status_message = 'Error with captcha: '+String(response['message']);
                };
            })
            .error(function(response) {
                console.log('Client error detected.');
                $scope.status_message = 'Got error while sending form to server.';
                grecaptcha.reset();
            });
    };
}]);