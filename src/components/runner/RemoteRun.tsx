export function buildRemoteRunCommand(path: string, config: { formattedCommand: string, msg?: string, url?: string }) {
  try {
      const command = config.formattedCommand;

      if (!command) {
          throw new Error("Command is required for remote execution.");
      }

      const envVariables = {
          '$PYTHON_PATH': path,
          '$XIRCUITS_PATH': path
      };

      let args = [
          ...command.trim().split(/\s+/),
          path,
          config['run_config_name'],
          config['project'],
          config['stage_out'],
          config['filesystem'],
          config['envName'],
          config['python'],
          config['modules'],
          config['libraries']];
      Object.keys(envVariables).forEach(key => {
          args = args.map(arg =>
            arg.replace(new RegExp(`\\${key}`, 'g'), envVariables[key])
          );
      });

      let code_str = "\nfrom subprocess import Popen, PIPE\n\n";
      code_str += `args= ${JSON.stringify(args)}\n`;
      code_str += "p=Popen(args, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=False)\n";
      code_str += "print('Remote Execution Run Mode.\\n')\n";
      code_str += `print(f'[COMMAND]\\n{args}\\n')\n`;

      if (config.url) {
          code_str += `print('[URL]\\nPlease go to ${config.url} for more details\\n')\n`;
      }

      if (config.msg) {
          code_str += `print('[MSG]\\n${config.msg}\\n')\n`;
      }

      code_str += "for line in p.stdout:\n";
      code_str += "    print(line.rstrip())\n\n";
      code_str += "if p.returncode != 0:\n";
      code_str += "    print(p.stderr.read())";

      return code_str;
  } catch (e) {
      console.log(e);
      throw e;
  }
}