#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to calculate the maximum profit with a knapsack capacity C
int unboundedKnapsack(int C, const vector<int> &weights, const vector<int> &profits)
{
    // DP array to store maximum profit for each capacity
    vector<int> dp(C + 1, 0);

    // Loop over all capacities from 1 to C
    for (int c = 1; c <= C; ++c)
    {
        for (int i = 0; i < weights.size(); ++i)
        {
            if (weights[i] <= c)
            {
                dp[c] = max(dp[c], dp[c - weights[i]] + profits[i]);
            }
        }
    }

    // The answer is stored in dp[C] (maximum profit for capacity C)
    return dp[C];
}

int main()
{
    // Define the weights and profits for the objects
    vector<int> weights = {4, 6, 8}; // object weights
    vector<int> profits = {7, 6, 9}; // object profits

    int capacity = 14; // knapsack capacity

    // Call the function and print the result
    int maxProfit = unboundedKnapsack(capacity, weights, profits);
    cout << "Maximum profit for capacity " << capacity << " is: " << maxProfit << endl;

    return 0;
}
