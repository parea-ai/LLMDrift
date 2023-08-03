# LLMDrift

Here is how you can reproduce this on Parea:

1. Sign-up for your free trial account
2. Upload the CSV in `datasets/primes_test.csv` on the Test Hub as a test collection
3. Create your custom evaluation functions or you can use the ones in the `evaluation_functions` folder
4. Save your API keys on the Settings page
5. Go to the Lab tab & create the prompts by:
   1. open a new session
   2. create all the prompts you want to test as columns
   3. save the session
6. go back to the Test Hub and click "Benchmark Prompts"
   1. name the evaluation benchmark run
   2. select the prompts
   3. select the evaluation metrics
   4. hit run!
