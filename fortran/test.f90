program three_x_plus_one
  implicit none
  
  integer(kind=16) :: n, input_n, max, total_n
  integer :: count, i, max_n, max_count
  integer :: start_time, end_time, elapsed_time, current_time
  integer :: percent
  
  call system_clock(start_time)

  total_n = 1000000000

  i = 1
  max_n = 0
  max_count = 0
  do while (i < total_n)
    i = i + 1
    n = i
    count = 0
    do while (n /= 1)
      count = count + 1
      if (mod(n, 2) == 0) then
        n = n / 2
      else
        n = 3 * n + 1
      end if
    end do
    if (count > max_count) then
      percent = int(100.0 * i / total_n)
      max_count = count
      max_n = i
      call system_clock(current_time)
      print *, max_n, max_count, percent, int(current_time - start_time)
    end if
  end do

  call system_clock(end_time)
  elapsed_time = end_time - start_time

  print *, max_n, max_count
  print *, elapsed_time, "ms"

end program three_x_plus_one

