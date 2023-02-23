program three_x_plus_one
  implicit none

  !boilerplate
  integer(kind=8) :: n, total_n
  integer :: count, i, max_n, max_count
  integer :: start_time, end_time, elapsed_time, current_time
  integer :: percent
  
  total_n = 1000000

  i = 1
  max_n = 0
  max_count = 0
  call system_clock(start_time)

  !calculate
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
      max_count = count
      max_n = i
    end if
  end do


  !print result
  call system_clock(end_time)
  elapsed_time = end_time - start_time

  print *, max_n, max_count
  print *, elapsed_time, "ms"

end program three_x_plus_one

