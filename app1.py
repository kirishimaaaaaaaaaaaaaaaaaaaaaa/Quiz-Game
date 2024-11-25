from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session handling

# Questions for all levels
questions_data = {
    1: [
        ["What does 'CPU' stand for?", "a) Central Processing Unit", "b) Computer Power Unit", "c) Central Programming Unit", "d) Computer Processing Unit", "a"],
        ["Which key combination is used to copy text on most computers?", "a) Ctrl + V", "b) Ctrl + X", "c) Ctrl + C", "d) Ctrl + Z", "c"],
        ["What is the main function of an operating system?", "a) Manage hardware and software resources", "b) Perform calculations", "c) Store user data", "d) Provide internet connectivity", "a"],
        ["What does 'RAM' stand for?", "a) Random Access Memory", "b) Read Access Memory", "c) Rapid Access Memory", "d) Reliable Access Memory", "a"],
        ["Which programming language is known as the mother of all languages?", "a) C", "b) Python", "c) Java", "d) Fortran", "a"],
        ["Which is the largest continent?", "a) Africa", "b) Asia", "c) Europe", "d) North America", "b"],
        ["What is the square root of 64?", "a) 6", "b) 7", "c) 8", "d) 9", "c"],
        ["Which planet is known as the Red Planet?", "a) Venus", "b) Earth", "c) Mars", "d) Jupiter", "c"],
        ["What is the capital of Japan?", "a) Seoul", "b) Beijing", "c) Tokyo", "d) Bangkok", "c"],
        ["What is the largest mammal?", "a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Shark", "b"],
    ],
    2: [
        ["What is the largest planet in the solar system?", "a) Earth", "b) Jupiter", "c) Saturn", "d) Mars", "b"],
        ["What is the chemical formula for water?", "a) CO2", "b) H2O", "c) O2", "d) CH4", "b"],
        ["Who invented the telephone?", "a) Alexander Graham Bell", "b) Thomas Edison", "c) Nikola Tesla", "d) Isaac Newton", "a"],
        ["Which continent is known as the 'Dark Continent'?", "a) Africa", "b) Asia", "c) Europe", "d) Australia", "a"],
        ["Which country has the largest population?", "a) India", "b) USA", "c) China", "d) Russia", "c"],
        ["Which is the tallest mountain in the world?", "a) K2", "b) Mount Everest", "c) Mount Kilimanjaro", "d) Mount Fuji", "b"],
        ["What is the capital of Australia?", "a) Sydney", "b) Melbourne", "c) Canberra", "d) Perth", "c"],
        ["Which programming language is primarily used for web development?", "a) Python", "b) Java", "c) JavaScript", "d) C++", "c"],
        ["What is the boiling point of water at sea level?", "a) 90°C", "b) 100°C", "c) 110°C", "d) 120°C", "b"],
        ["Which of these is a prime number?", "a) 4", "b) 6", "c) 7", "d) 8", "c"],
    ],
    3: [
        ["What is the largest desert in the world?", "a) Sahara", "b) Gobi", "c) Kalahari", "d) Antarctic Desert", "d"],
        ["Which of the following is a renewable energy source?", "a) Coal", "b) Oil", "c) Solar power", "d) Natural gas", "c"],
        ["What is the smallest country in the world?", "a) Vatican City", "b) Monaco", "c) San Marino", "d) Liechtenstein", "a"],
        ["Who painted the Mona Lisa?", "a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Michelangelo", "c"],
        ["What is the chemical symbol for gold?", "a) Au", "b) Ag", "c) Pb", "d) Fe", "a"],
        ["Who developed the theory of relativity?", "a) Isaac Newton", "b) Albert Einstein", "c) Nikola Tesla", "d) Galileo Galilei", "b"],
        ["What is the speed of light in a vacuum?", "a) 3×10^8 m/s", "b) 3×10^6 m/s", "c) 3×10^10 m/s", "d) 3×10^12 m/s", "a"],
        ["Which planet has the most moons?", "a) Earth", "b) Mars", "c) Saturn", "d) Jupiter", "c"],
        ["Which instrument is used to measure temperature?", "a) Barometer", "b) Thermometer", "c) Speedometer", "d) Altimeter", "b"],
        ["Which of the following is a mammal?", "a) Shark", "b) Whale", "c) Fish", "d) Crocodile", "b"],
    ],
    4: [
        ["What is the capital of Canada?", "a) Toronto", "b) Vancouver", "c) Ottawa", "d) Montreal", "c"],
        ["What is the most common element in the Earth's crust?", "a) Oxygen", "b) Carbon", "c) Iron", "d) Silicon", "a"],
        ["Which organ in the human body is responsible for pumping blood?", "a) Brain", "b) Heart", "c) Liver", "d) Lungs", "b"],
        ["Who was the first President of the United States?", "a) George Washington", "b) Thomas Jefferson", "c) Abraham Lincoln", "d) John Adams", "a"],
        ["What is the currency of Japan?", "a) Yuan", "b) Yen", "c) Ringgit", "d) Won", "b"],
        ["Which gas is most abundant in Earth's atmosphere?", "a) Oxygen", "b) Nitrogen", "c) Carbon dioxide", "d) Hydrogen", "b"],
        ["What is the largest internal organ in the human body?", "a) Heart", "b) Liver", "c) Lungs", "d) Brain", "b"],
        ["What is the primary ingredient in guacamole?", "a) Tomato", "b) Avocado", "c) Potato", "d) Onion", "b"],
        ["Which type of animal is the largest on Earth?", "a) Elephant", "b) Whale", "c) Giraffe", "d) Shark", "b"],
        ["What is the longest river in the world?", "a) Amazon River", "b) Nile River", "c) Yangtze River", "d) Mississippi River", "b"],
    ],
    5: [
        ["What is the formula for calculating the area of a circle?", "a) πr²", "b) 2πr", "c) πd", "d) r²", "a"],
        ["Who wrote 'Romeo and Juliet'?", "a) Charles Dickens", "b) William Shakespeare", "c) George Orwell", "d) Jane Austen", "b"],
        ["What is the hardest natural substance on Earth?", "a) Gold", "b) Diamond", "c) Iron", "d) Platinum", "b"],
        ["Which element has the atomic number 1?", "a) Hydrogen", "b) Oxygen", "c) Helium", "d) Carbon", "a"],
        ["Which country is known as the Land of the Midnight Sun?", "a) Russia", "b) Sweden", "c) Norway", "d) Finland", "c"],
        ["Who invented the lightbulb?", "a) Nikola Tesla", "b) Alexander Graham Bell", "c) Thomas Edison", "d) Albert Einstein", "c"],
        ["What is the main ingredient in traditional sushi?", "a) Chicken", "b) Beef", "c) Rice", "d) Fish", "c"],
        ["Which language is most spoken worldwide?", "a) English", "b) Spanish", "c) Mandarin", "d) Hindi", "c"],
        ["Which country is the Eiffel Tower located in?", "a) France", "b) Italy", "c) Spain", "d) Germany", "a"],
        ["Which type of animal is the fastest on Earth?", "a) Cheetah", "b) Lion", "c) Tiger", "d) Falcon", "a"],
    ]
}

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    level = session.get('level', 1)  # Get current level
    questions = questions_data[level]  # Get questions for the current level
    incorrect_answers = []  # To store questions with wrong answers

    if request.method == 'POST':
        score = 0
        for i, question in enumerate(questions):
            answer = request.form.get(f"question{i+1}")  # Get the selected answer
            correct_answer = question[-1]  # Correct answer from the question data
            
            # Compare the selected answer with the correct answer
            if answer == correct_answer:
                score += 1
            else:
                incorrect_answers.append((i + 1, question[0], correct_answer))  # Store wrong answers

        session['score'] = score  # Store the score in the session
        session['incorrect_answers'] = incorrect_answers  # Store incorrect answers in session

        # Check if user qualifies for the next level
        if score >= 9:
            if level < 5:  # If not the last level
                session['level'] = level + 1
                return redirect(url_for('quiz'))  # Proceed to the next level
            else:
                return redirect(url_for('result'))  # Final result
        else:
            return redirect(url_for('result'))  # Fail or final result
    
    return render_template('index.html', questions=questions, level=level)


@app.route('/result')
def result():
    score = session.get('score', 0)
    incorrect_answers = session.get('incorrect_answers', [])  # Retrieve from session
    level = session.get('level', 1)
    return render_template('result.html', score=score, level=level, incorrect_answers=incorrect_answers)

if __name__ == '__main__':
    app.run(port=5001, debug=True)