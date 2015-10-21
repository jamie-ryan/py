datset = ['si', 'mg', 'balmer', 'mgw', 'hmi']
nrb = 20

for i in datset:
    ii = str(i)
    with open('single-pixel-variable-names-'+ii+'.txt','a') as f:
        f.write("\n")
        for k in range(2):
            kk = str(k + 1)
            f.write('f'+i+'srb'+kk+ "\n")
            f.write('e'+i+'srb'+kk+ "\n")
            f.write('f'+i+'nrb'+kk+ "\n")
            f.write('e'+i+'nrb'+kk+ "\n")

        for i in datset:
            f.write("\n")
            f.write('t'+i+ "\n")
            f.write('f'+i+'qk' + "\n")
            f.write('e'+i+'qk' + "\n")
            for j in range(nrb):
                jj = str(j)
                f.write('f'+i+'rb'+jj+ "\n")
                f.write('e'+i+'rb'+jj+ "\n")

