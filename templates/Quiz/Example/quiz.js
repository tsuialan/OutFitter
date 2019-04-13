//Creation Date: 7/10/2015
//Description: This program provides a basic quiz application that enables individuals to
//             create personality quiz websites with no javascript knowledge. All that is 
//             needed is a basic understanding of HTML and some creativity. 




var currentQuestion = 2; //


/* 
	name: startQuiz
	desc: Removes all elements that are not needed after the
		   start of the quiz. 
	parameters: none
	returns: none
*/
function startQuiz() {
        document.getElementById("lore_brief").className = "invisible";
        document.getElementById("question-1").className = "question";
        var startBtn = document.getElementById('startQuizBtn');
        startBtn.parentNode.removeChild(startBtn);
    }
	
	
	
/* 
	name: getNumberOfQuestions
	desc: Used to dynamically get the  amount of questions 
		  that have been created on the HTML page. 
    parameters: none
    returns: totalQuestions
*/
function getNumberOfQuestions() {
        //QuerySelectorAll has better browser support in exchange for being slightly slower than gEBCN. 
        var totalQuestions = document.querySelectorAll('#quiz-questions .question').length;
        return totalQuestions;
    }
	
	

/* 
	name: nextQuestion
	desc: The primary tool for users to control their quiz position and 
		  executes functions in a way that promotes separation of interests.
    parameters: none
    returns: none
*/
function nextQuestion() {
        hideQuestion(currentQuestion);
        hideAnswerButton();
        showQuestion(currentQuestion);
        currentQuestion++;
    }
	

	
/* 
	name: setAnswerButton
	desc: Sets the visibility of the button element required to 
		  advance through questions to true. 
    parameters: none
    returns: none
*/
function setAnswerButton() {
        //yes, that's correct. this is my lazy way of input validation without annoyning users 
        //(e.g. transition on-click events) on the radio buttons...
        document.getElementById("confirm_answer").className = "";
    }



/* 
	name: hideAnswerButton
	desc: Assigns an invisible class (display: none;) to the button element 
		  required to advance through questions to true. 
    parameters: none
    returns: none
*/
function hideAnswerButton() {
        document.getElementById("confirm_answer").className = "invisible";
    }	
	
	

/* 
	name: hideQuestion
	desc: Hides the the question that a user has completed so the space
	can be swapped with another question. 
    parameters: id
    returns: none
*/
function hideQuestion(id) {
        var totalQuestions = getNumberOfQuestions();
        for (var i = 1; i <= totalQuestions; i++) {
            if (i !== id) {
                document.getElementById("question-" + i).className = "question invisible";
            }
        }
    }


	
/* 
	name: showQuestion
	desc: Will identify current question using ID parameter and
		  the invisible class free that have been created on the HTML page. 
    parameters: id
    returns: none
*/
function showQuestion(id) {
        var totalQuestions = getNumberOfQuestions();
        if (id <= totalQuestions) {
            document.getElementById("question-" + id).className = "question";
        } else {
			setEndingSentence() //begins the end screen process if id is above total question
        }
    }

/*
    name: getPersonality
    desc: obtains one of the four personalities of a person based on their quiz results
    parameters: id
    returns: integer representing one of the four personalities
function getPersonality(id) {
    /* 
     * Empty function: I wanted this to be more personalized instead of hardcoded. However, I
     * am not able to do this based on the lack of time.
     
}
*/


/* 
	name: getEndingSentence
	desc: Handles calculations and provides the necessary information for 
		  the quiz sentence genernation process to work. 
    returns: content
*/
function getEndingSentence() {
    var quizRadio = document.getElementsByName("rq");
	var content = ''; //It's easier to handle if we simply merge all sentences into a string
    for (var i = 0; i < quizRadio.length; i++) {
        if (quizRadio[i].checked) {
            content += quizRadio[i].getAttribute("data-endingsentence"); //these are the attributes used to generate quiz answers
        }
    }

/*  Legit data to match personality. However, we cannot do this and will instead hardcode to only dramatic
    // Dramatic = 1; Classic = 2; Trendy = 3; Conservative = 4
    if( getPersonality(id) ) {
        content += "On top of that, you love to make an entrance, attempting to "wow" people wherever you go. Your pattern \
                    choices always allows you to stand out amongst a large crowd, making them look simple compared to you. \
                    This makes shopping one of your favorite personalities, which is why you are so experienced at it.";
    } else if( classic ) {
        content += "Both simple and sophisticated, your fashion choice matches your simple yet elegant personality. You \
                    spend a necessary amount of time deciding which outfit matches both your personal preference and the \
                    situation you are in.";
    } else if( trendy ) {
        content += "You will catch on the trend before it even has a chance to go viral. Wearing the latest styles and \
                    cutting edge looks, you are on top of your game when it comes to ordering the fresh looks that are \
                    trending up-to-date.";
    } else {
        content += "There's nothing wrong with being a little too simple. You don't take any consideration when it comes \
                    to fashion sense, and that's okay. You have your own personal preference, and it is our job to match \
                    it. You can definitely count on us to not only match your preference but also provide you new and \
                    fresh looks that we know you will like."; 
    }
*/
    content += "On top of that, you love to make an entrance, attempting to 'wow' people wherever you go. Your pattern \
                    choices always allows you to stand out amongst a large crowd, making them look simple compared to you. \
                    This makes shopping one of your favorite personalities, which is why you are so experienced at it."
	return content;
}



/* 
	name: setEndingSentence
	desc: Collects information and outputs it to the HTML page.
    parameters: none
    returns: none
*/
function setEndingSentence() {
	var personalityResults = getEndingSentence();
    document.getElementById("results_screen").className = "";
	document.getElementById("generated_text").innerHTML = personalityResults; 

} 