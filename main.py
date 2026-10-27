import pandas as pd;
import matplotlib.pyplot as plt;
import os;

print("Data Visualisation!");

dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path = dir_path + "\\SolarPrediction.csv";

sp_df = pd.read_csv(dir_path);

def env_factors(f1,f2= "Radiation"):

    p_1 = sp_df[[f2,f1]]
    p_1_sort = p_1.sort_values(by=f1,ascending=True);
    
    print(p_1_sort)
    p_1_sort[f2] = p_1_sort[f2].astype(float);

    # p_1_sort[f1] = p_1_sort[f1].astype(float);

    plt.plot(p_1_sort[f2],   range(len(p_1_sort)),   '.',markersize=1.001, alpha=0.37);

    y_t_sort = list(range(0,len(p_1_sort),2000));
    y_t_sort.append(len(p_1_sort)-1);
    plt.yticks(y_t_sort,p_1_sort[f1].iloc[y_t_sort]);


    plt.xlabel(f2);
    plt.ylabel(f1);
    plt.title(f"Variation of {f2} with Time");
    plt.show()

# env_factors("Pressure");

while True:
    print("Solar Radiator-Analysis Predictor!");
    print("Which data do you want to analyze?");
    print("1:Variation of Solar Radiation with time \n 2:Relationship between Radiation and any environment variation\n 3:Other Graphs Plots to identify appropriate trends")
    print("4.Exit");

    u_r = int(input("Enter your response: "));

    if u_r ==1:
        env_factors("Time");
    
    elif u_r==2:

        print("These are the Environment Factors:");
        print(sp_df.columns.to_list()[1:9]);

        env_f = input("Enter the Environmental Factor you want to compare with!: ");

        env_factors(env_f);

    elif u_r==3:
        print(sp_df.columns.to_list()[1:9]);

        fc_1 = input("Enter the first factor:");
        fc_2 = input("Enter the second factor(Can't Time as the second Factor):");


        env_factors(fc_1,fc_2);

    else:
        print("Thanks for using our Program!");
        break;
