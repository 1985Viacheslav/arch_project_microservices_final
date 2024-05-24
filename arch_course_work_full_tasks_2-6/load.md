```
(GET)
Running 5s test @ http://127.0.0.1:8000/user/me
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   535.56ms  429.80ms   2.00s    47.57%
    Req/Sec   336.17    114.67   520.00     69.79%
  3215 requests in 5.04s, 822.59KB read
  Socket errors: connect 0, read 0, write 0, timeout 34
Requests/sec:    638.08
Transfer/sec:    163.26KB

(PATCH)
Running 5s test @ http://127.0.0.1:8000/user/me 
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.14s   447.00ms   2.00s    58.37%
    Req/Sec   138.37     52.09   262.00     72.41%
  1205 requests in 5.03s, 247.12KB read
  Socket errors: connect 0, read 0, write 0, timeout 201
Requests/sec:    239.43
Transfer/sec:     49.10KB

(GET)
Running 5s test @ http://127.0.0.1:8000/user/search/test
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   856.04ms  498.27ms   2.00s    65.68%
    Req/Sec   201.26     74.90   350.00     74.19%
  1867 requests in 5.04s, 515.98KB read
  Socket errors: connect 0, read 0, write 0, timeout 75
Requests/sec:    370.18
Transfer/sec:    102.31KB

(GET)
Running 5s test @ http://127.0.0.1:8000/user/?username=string
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   506.98ms  499.82ms   1.99s    82.73%
    Req/Sec   343.68     97.82   550.00     77.66%
  3237 requests in 5.03s, 796.61KB read
  Socket errors: connect 0, read 0, write 0, timeout 112
Requests/sec:    643.69
Transfer/sec:    158.41KB

(GET)
Running 5s test @ http://127.0.0.1:8000/user/get/23
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   820.02ms  493.12ms   2.00s    64.92%
    Req/Sec   215.66     73.07   383.00     72.53%
  1963 requests in 5.04s, 486.92KB read
  Socket errors: connect 0, read 0, write 0, timeout 73
Requests/sec:    389.42
Transfer/sec:     96.60KB

(POST)
Running 5s test @ http://127.0.0.1:8000/ptp_chat/send_message/23?message_text=wagw
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.13s   432.22ms   1.80s    75.99%
    Req/Sec   147.91     61.41   292.00     68.82%
  1398 requests in 5.04s, 368.61KB read
  Socket errors: connect 0, read 0, write 0, timeout 40
Requests/sec:    277.40
Transfer/sec:     73.14KB

(GET)
Running 5s test @ http://127.0.0.1:8000/ptp_chat/get_messages
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   528.11ms  614.63ms   1.97s    78.39%
    Req/Sec   123.11     75.11   330.00     62.22%
  1118 requests in 5.05s, 38.26MB read
  Socket errors: connect 0, read 0, write 0, timeout 174
Requests/sec:    221.40
Transfer/sec:      7.58MB

(POST)
Running 5s test @ http://127.0.0.1:8000/group_chat/send_message/66423e7b8d010f4802b6b701?message_text=svd
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   816.90ms  652.11ms   1.95s    45.72%
    Req/Sec   138.28     62.42   270.00     66.30%
  1307 requests in 5.05s, 343.34KB read
  Socket errors: connect 0, read 0, write 0, timeout 209
Requests/sec:    258.88
Transfer/sec:     68.01KB

(GET)
Running 5s test @ http://127.0.0.1:8000/group_chat/66423e7b8d010f4802b6b701
  2 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   432.79ms  577.40ms   1.96s    83.17%
    Req/Sec   101.74     45.60   190.00     60.82%
  989 requests in 5.04s, 43.32MB read
  Socket errors: connect 0, read 0, write 0, timeout 163
Requests/sec:    196.21
Transfer/sec:      8.59MB



```