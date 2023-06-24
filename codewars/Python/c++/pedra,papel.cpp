#include <string>

std::string rps(const std::string& p1, const std::string& p2)
{
    std::string word1 = p1;
    std::string word2 = p2;

    if ((word1 == "rock" && word2 == "scissor") || (word2 == "rock" && word1 == "scissor"))
    {
        if (word1 == "rock")
        {
            return "Player 1 won!";
        }
        else
        {
            return "Player 2 won!";
        }
    }
    if ((word1 == "paper" && word2 == "scissor") || (word2 == "scissor" && word1 == "paper"))
    {
        if (word1 == "scissor")
        {
            return "Player 1 won!";
        }
        else
        {
            return "Player 2 won!";
        }
    }
    if ((word1 == "paper" && word2 == "rock") || (word2 == "paper" && word1 == "rock"))
    {
        if (word1 == "paper")
        {
            return "Player 1 won!";
        }
        else
        {
            return "Player 2 won!";
        }
    }
    if ((word1 == "paper" && word2 == "paper") || (word1 == "rock" && word2 == "rock") || (word1 == "scissor" && word2 == "scissor"))
    {
        return "Draw!";
    }

    return "";
}